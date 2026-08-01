import os
import tempfile

import streamlit as st

from config import FAISS_INDEX_FILE
from rag.indexing_pipeline import IndexingPipeline
from rag.rag_pipeline import RAGPipeline
from ui.styles import load_css


# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Study Buddy - Learning RAG",
    page_icon="📚",
    layout="wide",
)

# ----------------------------------------------------
# LOAD CSS
# ----------------------------------------------------

st.markdown(
    load_css(),
    unsafe_allow_html=True,
)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------

st.markdown(
    """
    <div class="header-card">

    <div class="header-title">
    📚 Study Buddy
    </div>

    <div class="header-subtitle">
    Learn Retrieval-Augmented Generation (RAG)
    using FAISS + Sentence Transformers + Ollama
    </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------
# SESSION STATE
# ----------------------------------------------------

if "document_indexed" not in st.session_state:
    st.session_state.document_indexed = False

# ----------------------------------------------------
# LAYOUT
# ----------------------------------------------------

left_col, right_col = st.columns([1, 2])

# ====================================================
# SIDEBAR PANEL
# ====================================================

with left_col:

    st.markdown(
        '<div class="card-title">📂 Upload Document</div>',
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Supported Files",
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg",
            "txt",
        ],
    )

    if uploaded_file:

        st.success("File uploaded successfully.")

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=os.path.splitext(uploaded_file.name)[1],
        ) as temp_file:

            temp_file.write(uploaded_file.read())

            temp_path = temp_file.name

        if st.button(
            "📚 Create Index",
            use_container_width=True,
        ):

            with st.spinner(
                "Creating vector index..."
            ):

                try:

                    indexer = IndexingPipeline()

                    total_chunks = indexer.index_document(
                        temp_path
                    )

                    st.session_state.document_indexed = True

                    st.success(
                        f"""
                        Index Created Successfully!

                        Total Chunks:
                        {total_chunks}
                        """
                    )

                except Exception as e:

                    st.error(str(e))

    st.markdown("---")

    st.markdown("### 📈 Status")

    if FAISS_INDEX_FILE.exists():

        st.success("FAISS Index Ready")

    else:

        st.warning("No Index Found")

# ====================================================
# MAIN PANEL
# ====================================================

with right_col:

    st.markdown(
        '<div class="card-title">🤖 Ask Your Document</div>',
        unsafe_allow_html=True,
    )

    mode = st.selectbox(

        "Choose Mode",

        [
            "ask",
            "summary",
            "topics",
            "questions",
            "quiz",
            "flashcards",
        ],
    )

    question = ""

    if mode == "ask":

        question = st.text_input(
            "Enter your question"
        )

    if st.button(
        "🚀 Generate",
        use_container_width=True,
    ):

        try:

            if not FAISS_INDEX_FILE.exists():

                st.warning(
                    "Please upload and index a document first."
                )

            else:

                pipeline = RAGPipeline()

                with st.spinner(
                    "Thinking..."
                ):

                    response = pipeline.run(

                        mode=mode,

                        user_input=question,

                    )

                st.markdown(
                    """
                    <div class="card-title">
                    📄 Response
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.markdown(
                    f"""
                    <div class="result-card">

                    {response}

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        except Exception as e:

            st.error(str(e))

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.markdown("---")

st.caption(
    "Built for Learning ❤️ | FAISS • Sentence Transformers • Ollama • Streamlit"
)