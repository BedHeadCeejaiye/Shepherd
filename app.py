import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="The Shepherd's Pasture",
    page_icon="🐑",
    layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🐑 The Shepherd's Pasture")
st.caption("Click inside the game box, then use **WASD** or **Arrow Keys** to move.")

# Load the external HTML file safely
html_path = os.path.join(os.path.dirname(__file__), "game.html")
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        game_html = f.read()
    components.html(game_html, height=540)
else:
    st.error("Error: Could not find `game.html` in the project directory.")

with st.expander("About this game"):
    st.write("A simple peaceful farming game... or is it? Collect items and explore your surroundings.")
