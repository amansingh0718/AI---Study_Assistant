from pathlib import Path

import streamlit as st


def load_css():
    """
    Load external CSS file.
    """

    css_file = Path("assets/styles.css")

    if css_file.exists():

        with open(
            css_file,
            "r",
            encoding="utf-8"
        ) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )