import streamlit as st
from googletrans import Translator

translator = Translator()

st.set_page_config(page_title="AI Marketplace Assistant", layout="centered")

st.title("🧵 AI-Powered Marketplace Assistant for Local Artisans")

st.subheader("👩‍🎨 Add Your Product")
artisan_text = st.text_area("Enter product details in your local language", "")

if st.button("Translate & Generate Listing"):
    if artisan_text.strip():
        translation = translator.translate(artisan_text, dest='en')
        st.success(f"✅ English Description: {translation.text}")
        keywords = ["handmade", "eco-friendly", "traditional", "local", "unique"]
        st.info("✨ Suggested Tags: " + ", ".join(keywords[:3]))
    else:
        st.warning("Please enter some product details.")

st.subheader("🛒 Product Recommendations")
products = ["Handmade Pottery", "Organic Cotton Saree", "Bamboo Basket", "Terracotta Jewelry"]
choice = st.selectbox("Choose a product you like", products)

if st.button("Get Recommendations"):
    if choice == "Handmade Pottery":
        st.write("👉 You may also like: Clay Cups, Painted Pots")
    elif choice == "Organic Cotton Saree":
        st.write("👉 You may also like: Khadi Dress, Linen Saree")
    elif choice == "Bamboo Basket":
        st.write("👉 You may also like: Bamboo Mat, Cane Furniture")
    elif choice == "Terracotta Jewelry":
        st.write("👉 You may also like: Stone Necklace, Beaded Earrings")
