import streamlit as st
import google.generativeai as genai


API_KEY = "AIzaSyCbALySK79txE-LP7_4gB3EbLGMKfq4PCI"  


genai.configure(api_key=API_KEY)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "You are a finance helper model. Your task is to suggest investment schemes "
        "suitable for women based on their annual investment, desired returns, and any "
        "special cases provided. Focus on government schemes but do not exclude other "
        "reliable options. Provide the full name of the scheme, its benefits, eligibility "
        "criteria, and step-by-step guidance on how to enroll."
        "include loan sugessions also"
    ),
)

st.title("Investment Scheme Suggestion")
st.write("Provide your details to get personalized investment scheme recommendations.")

investment_per_year = st.number_input("Investment per Year (in ₹):", min_value=0.0, step=1000.0, format="%.2f")
expected_returns = st.number_input("Expected Returns (in %):", min_value=0.0, step=0.1, format="%.2f")
special_cases = st.text_area("Special Cases (e.g., 'single mother', 'retirement planning', etc.):")

if st.button("Get Suggestions"):
    if investment_per_year > 0 and expected_returns > 0:
       
        user_input = (
            f"My annual investment is ₹{investment_per_year:.2f}, and I am expecting returns "
            f"of {expected_returns:.2f}%. Special considerations: {special_cases}."
        )
        
        try:
            
            chat_session = model.start_chat(history=[])
            response = chat_session.send_message(user_input)
            
            
            st.subheader("Suggested Investment Scheme")
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please provide valid inputs for both investment and expected returns.")
