import streamlit as st
import google.generativeai as genai
import os

# Set Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAEy_nSYu0jh5t0aKB48dyGDdXpajRVoCo"

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model
def get_gemini_response(input_text, language):
    # Define language-specific prompts
    prompts = {
        "हिंदी": f"प्रश्न: {input_text}\nउत्तर:",
        "मराठी": f"प्रश्न: {input_text}\nउत्तर:",
        "തമിഴ്": f"கேள்வி: {input_text}\nபதில்:",
        "తెలుగు": f"ప్రశ్న: {input_text}\nసమాధానం:",
        "ಕನ್ನಡ": f"ಪ್ರಶ್ನೆ: {input_text}\nಉತ್ತರ:",
        "English": f"Question: {input_text}\nAnswer:"
    }

    # Generate response using the few-shot learning technique
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompts[language])
    return response.text

# Streamlit app initialization
st.set_page_config(page_title="Krishi Sahayak (कृषि सहायक)", page_icon="🌾")  # Hindi for Agri Assistant

# Title with a symbol and styling
st.title("कृषि सहायक (कृषि सहायक) ")  # Hindi for Agri Assistant with Wheat symbol
st.markdown("<p style='text-align: center; font-size: 18px;'>शेती संबंधित प्रश्नांची उत्तरे!</p>", unsafe_allow_html=True)

# Language selection with Indian languages and styling
language_options = ["हिंदी", "मराठी", "തമിഴ്", "తెలుగు", "ಕನ್ನಡ", "English"]
language = st.selectbox("भाषा (Language)", language_options, index=1, format_func=lambda x: f"🌐 {x}")  # Use emoji for better UI

# Application prompt with better UI
st.markdown("""
<h3 style="text-align: center; color: #1E703C;">आपल्या शेतीशी संबंधित काही प्रश्न आहेत का? </h3>
<p style="text-align: center;">आपल्याला पीक, खत, किडबी नियंत्रण, किंवा शेतीसंबंधित कोणत्याही प्रश्नांची उत्तरे मिळवा!</p>
<p style="text-align: center;">कृपया खाली आपला प्रश्न टाइप करा आणि "उत्तर मिळवा" बटण दाबा.</p>
""", unsafe_allow_html=True)  # Allow HTML formatting for better UI

# Add image related to agriculture
st.image("D:/CHATBOT/Agriculture.jpg", 
         caption="", use_column_width=True)

# Text input for user query with styling
input_text = st.text_input("तुमचा प्रश्न / Your Question", "")

# Button to trigger chatbot response with a symbol and styling
if st.button("उत्तर मिळवा (Get Response) 🚀"):
    if input_text.strip() == "":
        st.warning("कृपया एक प्रश्न प्रविष्ट करा / Please enter a question.")
    else:
        response = get_gemini_response(input_text, language)
        st.subheader("उत्तर (Response):" if language != "English" else "Response:")
        st.write(response)
