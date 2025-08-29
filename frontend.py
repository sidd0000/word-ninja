import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/split"

st.set_page_config(page_title="Word Splitter", page_icon="✂️", layout="centered")

# Title
st.title("✂️ Joined Words Splitter")
st.markdown("Enter a joined word or phrase and get the split words using FastAPI backend.")

# Input box
user_input = st.text_input("Enter text to split:", placeholder="Type something like 'everyonehereafter'")

if st.button("Split Words"):
    if not user_input.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            # Send request to FastAPI backend
            response = requests.post(API_URL, json={"text": user_input})
            
            if response.status_code == 200:
                words = response.json().get("words", [])
                
                if words:
                    st.success("✅ Words split successfully!")
                    st.write("### Result:")
                    
                    # Display words as styled chips
                    st.markdown(
                        " ".join([f"<span class='chip'>{w}</span>" for w in words]),
                        unsafe_allow_html=True
                    )
                else:
                    st.error("❌ Could not split words.")
            else:
                st.error(f"🚨 Error: {response.json().get('detail')}")
        except Exception as e:
            st.error(f"⚡ Backend not reachable: {e}")

# CSS for styling word chips
st.markdown(
    """
    <style>
    .chip {
        display: inline-block;
        padding: 8px 15px;
        margin: 5px;
        border-radius: 20px;
        background-color: #FFE08A;
        color: black;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .chip:hover {
        background-color: #ffcc33;
        transform: scale(1.1);
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)
