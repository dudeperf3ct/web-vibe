"""Streamlit to visualize results."""

import streamlit as st
import json
import os

DATA_DIR = "data"


def main():
    """Streamlit entrypoint."""

    st.title("Web Vibe")
    data_path = f"{DATA_DIR}/analysis.json"
    # Check if results file is present
    if not os.path.exists(data_path):
        raise ValueError("Run `main.py` to create a analysis json file.")

    with open(data_path, "r") as fp:
        data = json.load(fp)

    urls = [d["url"] for d in data]
    selected_url = st.selectbox(label="Select website to analyse", options=urls)
    selected_index = urls.index(selected_url)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(data[selected_index]["screenshot"])
    with col2:
        st.write(data[selected_index]["llm_response"])
    with col3:
        st.write(data[selected_index]["rewrite_content"])


if __name__ == "__main__":
    main()
