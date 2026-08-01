import os
import tempfile

import streamlit as st

from config import FAISS_INDEX_FILE

from rag.indexing_pipeline import IndexingPipeline
from rag.rag_pipeline import RAGPipeline


st.set_page_config(
    page_title="Simple RAG Learning Project",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Simple RAG Learning Project")

st.write(
    "Upload a PDF, Image or TXT file and ask questions."
)

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["pdf", "png", "jpg", "jpeg", "txt"]
)

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=os.path.splitext(uploaded_file.name)[1]
    ) as temp_file:

        temp_file.write(
            uploaded_file.read()
        )

        temp_path = temp_file.name

    if st.button("Create Index"):

        with st.spinner(
            "Indexing document..."
        ):

            try:

                indexer = IndexingPipeline()

                total_chunks = indexer.index_document(
                    temp_path
                )

                st.success(
                    f"Document indexed successfully!\n\nChunks Created: {total_chunks}"
                )

            except Exception as e:

                st.error(str(e))

st.divider()

mode = st.selectbox(

    "Select Mode",

    [
        "ask",
        "summary",
        "topics",
        "questions",
        "quiz",
        "flashcards"
    ]
)

question = ""

if mode == "ask":

    question = st.text_input(
        "Enter your question"
    )

if st.button("Generate"):

    try:

        # Check whether FAISS index exists
        if not FAISS_INDEX_FILE.exists():

            st.warning(
                "Please upload and index a document first."
            )

        else:

            pipeline = RAGPipeline()

            with st.spinner(
                "Generating response..."
            ):

                response = pipeline.run(

                    mode=mode,

                    user_input=question

                )

            st.subheader("Result")

            st.write(response)

    except Exception as e:

        st.error(str(e))