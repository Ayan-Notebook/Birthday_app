import streamlit as st

st.set_page_config(page_title="Happy Birthday 🎉", layout="wide")

st.title("🎂 Happy Birthday Special Page 🎂")
st.write("Enjoy the surprise below! 👇")

# Embed the external HTML
html_code = """
<iframe src="http://localhost:8000" width="100%" height="900px" style="border:none;"></iframe>
"""
st.components.v1.html(html_code, height=900)