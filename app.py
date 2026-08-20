# Import required libraries for environment handling, Groq inference, image processing, encoding, and building the Streamlit web app
import os
from groq import Groq
import streamlit as st
import base64
from PIL import Image
# from dotenv import load_dotenv
# load_dotenv()


# Set up model and securely load authentication token
model = "meta-llama/llama-4-maverick-17b-128e-instruct"

groq_api_key = os.environ["GROQ_API_KEY"]

# Initialize client (do once)
client = Groq(api_key=groq_api_key)

#page configuration
st.set_page_config(
    page_title="MedHelp AI",
    page_icon="📝",
    layout="centered"
)

st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-left: 3rem;
            padding-right: 3rem;
            max-width: 1200px;
        }
    </style>
""", unsafe_allow_html=True)

# Load image
logo = Image.open("logo.png")

# Create columns
col1, col2 = st.columns([1, 12], gap="small")

with col1:
    st.markdown(
        """
        <style>
        .logo-img {
            border-radius: 50%;
            border: 3px solid #4CAF50;
            width: 80px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.image(logo, width=80)

with col2:
    st.markdown(
        "<h1 style='margin-bottom:0;'>MedHelp AI - Medical Image Intelligence</h1>",
        unsafe_allow_html=True
    )

# Subheader below
st.subheader("AI-powered analysis of medical images to assist early insights and understanding")

#function for response generation
def generate_medical_response(prompt: str, image_base64: str = None):
    """
    Generate response from Llama 4 Maverick (via Groq) using text + optional image

    Args:
        prompt (str): Your structured medical prompt
        image_base64 (str): Base64 encoded image (optional)

    Returns:
        str: Model response
    """

    # Build content
    content = []

    if image_base64:
        content.append(
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            }
        )

    content.append({"type": "text", "text": prompt})

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a safe and responsible medical AI assistant."
                },
                {
                    "role": "user",
                    "content": content
                }
            ],
            temperature=0.3,      # 🔥 more reliable for medical use
            top_p=0.9,
            max_tokens=2000,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating response: {str(e)}"

#conversion to base64
def convert_to_base64(uploaded_file):
    return base64.b64encode(uploaded_file.read()).decode("utf-8")

#structured prompt 
prompt = """
You are an advanced AI medical visual assistant that analyzes images of possible health symptoms.

Your goal is to provide a structured, safe, and helpful analysis based ONLY on what is visible in the image.

----------------------------------------
🚨 SAFETY RULES (STRICT)
----------------------------------------
- You are NOT a doctor.
- Do NOT provide a definitive diagnosis.
- Always express uncertainty (use: "may", "could", "possibly").
- Do NOT prescribe medications or dosages.
- Encourage consulting a qualified medical professional when needed.
- If something appears serious, clearly recommend immediate medical attention.

----------------------------------------
🧠 ANALYSIS INSTRUCTIONS
----------------------------------------

### 1. Visual Observations
Describe ONLY what is visible:
- Body part (if identifiable)
- Color (redness, pale, dark, etc.)
- Shape, size, and distribution
- Texture (smooth, rough, blistered, swollen)
- Any visible signs (rash, cuts, swelling, pus, bleeding, discoloration)

---

### 2. Possible Conditions
List 3–5 possible conditions.

For each:
- **Condition Name**
- **Why it may match**
- **Confidence:** Low / Medium / High

⚠️ Do NOT conclude or confirm any condition.

---

### 3. Related Symptoms
List commonly associated symptoms:
- Pain / itching / burning
- Fever / fatigue
- Duration patterns

---

### 4. Severity Assessment
Classify as ONE:
- 🟢 Mild  
- 🟡 Moderate  
- 🟠 Potentially Serious  
- 🔴 Emergency  

Explain briefly.

---

### 5. General Advice
Provide safe, general guidance:
- Hygiene tips
- What to avoid
- General OTC suggestions (no dosage)

---

### 6. When to Seek Medical Help
Clearly mention:
- Warning signs
- When condition worsens
- Time thresholds

---

----------------------------------------
📌 OUTPUT FORMAT (STRICT)
----------------------------------------

⚠️ Informational only — not a medical diagnosis.

## 🩺 Visual Observations
...

## 🤔 Possible Conditions
- Condition 1  
- Condition 2  

## 📋 Related Symptoms
...

## ⚖️ Severity Assessment
...

## 💡 General Advice
...

## 🚑 When to Seek Medical Help
...

----------------------------------------
🎯 TONE
----------------------------------------
- Calm, supportive, and clear
- Simple language
- No unnecessary medical jargon

----------------------------------------
❗ EDGE CASE
----------------------------------------
If the image is unclear:
- Clearly say so
- Ask for a better image or more details
"""    

#file upload
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

#show uploaded file
if uploaded_file:
    st.image(uploaded_file, width=250, caption="Uploaded image")
    uploaded_file.seek(0)  # 🔥 reset pointer

#submit button
submit_button = st.button("Generate Analysis")

#after submission
if submit_button:
    if not uploaded_file:
        st.error("Please upload an image first")
    else:
        image_base64 = convert_to_base64(uploaded_file)

        with st.spinner("🔍 Generating medical analysis..."):
            result = generate_medical_response(prompt, image_base64)

        st.write(result)