import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time
import langchain_helper

# Page configuration
st.set_page_config(page_title="Restaurant Name Generator", page_icon="🍽️", layout="centered")

# Custom CSS for gradient background and aesthetic buttons
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ffecd2, #fcb69f);
        color: #333333;
    }
    .stButton > button {
        background-color: #a796e8;
        color: white;
        border-radius: 12px;
        padding: 0.75em 1.5em;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .stButton > button:hover {
        background-color: #cdb5ff;
        transform: scale(1.05);
    }
    .fade-in {
        animation: fadeIn 2s;
    }
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Lottie animation loader
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animation
lottie_food = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_Cc8Bpg.json")

# Title and animation
st.title("🍽️ Restaurant Name Generator")
st_lottie(lottie_food, speed=0.7, height=300, key="food")

# Cuisine selector
cuisine = st.sidebar.selectbox(
    "Pick Cuisine",
    (
        "Argentinian", "Australian", "Austrian", "Belgian", "Brazilian", "Canadian",
        "Chinese", "Cuban", "Danish", "Egyptian", "Ethiopian", "French", "German", "Greek",
        "Indian", "Indonesian", "Iranian", "Iraqi", "Irish", "Israeli", "Italian", "Jamaican",
        "Japanese", "Jordanian", "Korean", "Lebanese", "Malaysian", "Mexican", "Moroccan",
        "Nepalese", "Dutch", "Nigerian", "Peruvian", "Filipino", "Polish", "Portuguese",
        "Russian", "Saudi Arabian", "Singaporean", "South African", "Spanish", "Sri Lankan",
        "Swedish", "Swiss", "Syrian", "Taiwanese", "Thai", "Turkish", "British", "Vietnamese"
    )
)

# Generate restaurant button
if st.button("Generate Restaurant"):
    with st.spinner("Crafting your restaurant..."):
        time.sleep(1.5)  # Simulate loading
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    # Fade-in effect using CSS class
    st.markdown(f"""🍴{response['restaurant_name'].strip()}""", unsafe_allow_html=True)
    
    menu_items = response['menu_items'].strip().split(",")
    st.write("### Menu Items")

    for item in menu_items:
        st.markdown(f"{item.strip()}", unsafe_allow_html=True)
