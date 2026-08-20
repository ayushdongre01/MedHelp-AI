# 🏥 MedHelp AI - Medical Image Intelligence

**AI-powered analysis of medical images to assist early insights and understanding**

An intelligent medical imaging assistant powered by Qwen's multimodal model via Groq inference, designed to help users understand potential health concerns through visual analysis of medical images. This tool leverages advanced multimodal AI to provide structured, safe, and responsible medical insights.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [Safety Features](#safety-features)
- [Sample Images](#sample-images)
- [Live Demo](#live-demo)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

---

## Overview

**MedHelp AI** is a Streamlit-based web application designed to analyze medical images and provide structured health insights. The application uses the `qwen/qwen3.6-27b` model via **Groq's inference API** to deliver:

- **Visual Analysis** - Detailed examination of medical images
- **Possible Conditions** - List of potential health conditions with confidence levels
- **Severity Assessment** - Categorized severity ratings (Mild → Emergency)
- **General Guidance** - Safe, non-prescriptive health advice
- **Safety Warnings** - Clear guidance on when to seek professional medical help

> **⚠️ IMPORTANT**: This tool is **informational only** and is **not a substitute for professional medical diagnosis or treatment**. Always consult a qualified healthcare professional.

---

## Features

### 🎯 Core Capabilities

- **Multimodal AI Analysis** - Combines image recognition with medical knowledge
- **Structured Output** - Organized, easy-to-read format for medical insights
- **Safety-First Design** - Built-in constraints and disclaimers
- **Real-time Processing** - Fast, low-latency responses via Groq's inference engine
- **Multiple Image Formats** - Supports PNG, JPG, and JPEG images
- **Clean UI** - Intuitive Streamlit interface with custom styling

### 🔒 Safety Guarantees

- No definitive diagnoses provided
- Consistent use of cautious language ("may", "could", "possibly")
- No medication prescriptions or dosages
- Clear emergency warning indicators
- Professional consultation recommendations

### 📊 Analysis Sections

1. **Visual Observations** - What's visible in the image
2. **Possible Conditions** - 3-5 potential conditions with confidence levels
3. **Related Symptoms** - Common associated symptoms
4. **Severity Assessment** - Color-coded severity levels (🟢🟡🟠🔴)
5. **General Advice** - Safe hygiene and care tips
6. **When to Seek Medical Help** - Warning signs and time thresholds

---

## Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Web UI framework |
| **AI Model** | Qwen (`qwen/qwen3.6-27b`) | Medical image analysis |
| **Model Provider** | Groq API | Low-latency inference endpoint for the model |
| **Image Processing** | PIL (Pillow) | Image handling & display |
| **Authentication** | Groq API Key (env variable) | Secure API access |
| **Environment** | Python 3.8+ | Runtime environment |

### Dependencies

```
streamlit    # Web framework
groq         # Groq inference API client
Pillow       # Image processing
```

> Note: `python-dotenv` is optional — the app can load `GROQ_API_KEY` directly from your shell environment, or from a `.env` file if you uncomment the relevant lines in `app.py`.

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- A Groq account and API key ([console.groq.com](https://console.groq.com))

### Step 1: Clone or Download

```bash
# Download the project
cd MedHelp\ AI
```

### Step 2: Create Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Set your Groq API key as an environment variable:

```bash
# Windows
set GROQ_API_KEY=your_groq_api_key_here

# macOS/Linux
export GROQ_API_KEY=your_groq_api_key_here
```

Or create a `.env` file in the project root and uncomment the `dotenv` lines at the top of `app.py`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Step 5: Add Logo

Place a `logo.png` file (recommended 300x300px) in the project root directory. This will display in the app header.

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## Configuration

### API Settings

The application uses the following default configuration:

```python
PROVIDER: Groq (https://api.groq.com)
MODEL: qwen/qwen3.6-27b
```

**To change the model**, edit [app.py](app.py):

```python
model = "your_desired_model_here"
```

### Model Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `temperature` | 0.3 | Lower = more deterministic responses (ideal for medical) |
| `top_p` | 0.9 | Balanced diversity in outputs |
| `max_tokens` | 2000 | Maximum response length |
| `reasoning_format` | `"hidden"` | Suppresses internal `<think>...</think>` reasoning from the output |

---

## Usage Guide

### Basic Workflow

1. **Open Application**
   ```bash
   streamlit run app.py
   ```

2. **Upload Medical Image**
   - Click "Upload an image" button
   - Select PNG, JPG, or JPEG file
   - Image preview will display (max width: 250px)

3. **Generate Analysis**
   - Click "Generate Analysis" button
   - Wait for AI processing (typically a few seconds thanks to Groq's fast inference)
   - Structured medical insights will appear

4. **Review Results**
   - Read all sections carefully
   - Pay special attention to severity assessment
   - Note recommendations for professional help

### Example Analysis Output

```
⚠️ Informational only — not a medical diagnosis.

## 🩺 Visual Observations
- Body part: Right forearm
- Color: Red with slight swelling
- Distribution: Localized to small area
- Texture: Inflamed skin surface

## 🤔 Possible Conditions
- Contact Dermatitis (High confidence)
- Eczema (Medium confidence)
- Heat Rash (Medium confidence)

## 📋 Related Symptoms
- Itching or burning sensation
- Possible mild fever
- Usually develops within hours

## ⚖️ Severity Assessment
🟡 Moderate - Localized inflammation without systemic symptoms

## 💡 General Advice
- Keep area clean and dry
- Avoid scratching
- Use mild soap for washing
- Avoid known allergens

## 🚑 When to Seek Medical Help
- If rash spreads or worsens
- If swelling increases significantly
- If fever develops: seek immediate care
- If symptoms persist beyond 2 weeks
```

### Tips for Best Results

✅ **Good Images:**
- Clear, well-lit photos
- Minimal shadows or glare
- Appropriate zoom (shows affected area clearly)
- Consistent color temperature

❌ **Poor Images:**
- Blurry or out of focus
- Low lighting
- Extreme angles
- Too zoomed in or out

---

## Safety Features

### Built-in Medical Safeguards

1. **Non-Diagnostic Language**
   - Uses probabilistic terms: "may", "could", "possibly"
   - Never uses absolute conclusions

2. **Emergency Indicators**
   - 🔴 Emergency level triggers specific urgent advice
   - Clear warning signs listed
   - Immediate consultation recommended

3. **Low Temperature Setting**
   - Temperature: 0.3 (lower = more reliable)
   - Reduces hallucinations and unreliable outputs
   - Essential for medical accuracy

4. **Structured Prompt System**
   - Enforces specific analysis format
   - Prevents off-topic responses
   - Ensures comprehensive coverage

5. **Professional Consultation Emphasis**
   - Every analysis includes "when to seek help"
   - Regular reminders: "not a doctor"
   - Liability disclaimer in header

---

## Sample Images

### Image Categories Supported

This application can analyze images of:

- **Skin Conditions**: Rashes, acne, eczema, psoriasis, hives
- **Wounds & Injuries**: Cuts, bruises, burns, blisters
- **Inflammation**: Swelling, redness, edema
- **Infections**: Signs of bacterial or fungal infection
- **Other**: Visible symptoms of general health concerns

### Sample Images

Below are sample outputs demonstrating the analysis of medical images generated by MedHelp AI:

![MedHelp AI – Sample Image 1](https://github.com/ayushdongre01/MedHelp-AI/blob/main/images/1.png)
![MedHelp AI – Sample Image 2](https://github.com/ayushdongre01/MedHelp-AI/blob/main/images/2.png)
![MedHelp AI – Sample Image 3](https://github.com/ayushdongre01/MedHelp-AI/blob/main/images/3.png)
![MedHelp AI – Sample Image 4](https://github.com/ayushdongre01/MedHelp-AI/blob/main/images/4.png)

### Where to Get Test Images

- **Public Medical Libraries**: WebMD, Cleveland Clinic
- **Educational Resources**: Medical textbooks, academic databases
- **Safe Options**: Create controlled, safe examples with permission
- **Stock Medical Images**: Properly licensed medical image databases

> ⚠️ Always obtain proper consent before using real patient images

---

## Live Demo

### Option 1: Local Demo

Run the application locally to explore features:

```bash
streamlit run app.py
```

**Demo Login:** No authentication required  
**Demo Duration:** Unlimited (local)  
**API Cost:** Depends on your Groq usage/quota

### Option 2: Deployed Demo

👉 Try the app here:  
🔗 [https://medapp-ai.streamlit.app/](https://medapp-ai.streamlit.app/)

### Interactive Features to Try

- ✅ Upload different image formats (PNG, JPG, JPEG)
- ✅ Test with various medical conditions
- ✅ Review severity assessment changes
- ✅ Compare multiple image analyses
- ✅ Test UI responsiveness on mobile

---

## Project Structure

```
MedHelp AI/
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
├── logo.png                 # Application logo (optional)
├── .gitignore               # Git ignore rules
├── README.md                # This file
```

### File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Main application logic, UI components, API integration |
| `requirements.txt` | Python package dependencies |
| `logo.png` | App header logo/branding |
| `.env` | Environment variables (`GROQ_API_KEY`), optional |

---

## Troubleshooting

### ❌ Issue: "Error generating response: Invalid API key" / authentication errors

**Cause**: Groq API key is invalid, expired, or missing  
**Solution**:
1. Verify `GROQ_API_KEY` is set correctly in your environment (or `.env` file)
2. Confirm the key is active in your [Groq console](https://console.groq.com)
3. Regenerate the key if needed
4. Restart the application

```bash
# Verify the key is set
echo $GROQ_API_KEY   # macOS/Linux
echo %GROQ_API_KEY%  # Windows
```

### ❌ Issue: `KeyError: 'GROQ_API_KEY'`

**Cause**: The environment variable isn't set before the app starts  
**Solution**: Export/set `GROQ_API_KEY` in your shell (or `.env` file with dotenv enabled) before running `streamlit run app.py`.

### ❌ Issue: "Unable to locate logo.png"

**Cause**: Logo file not found in project root  
**Solution**:
1. Add `logo.png` to project root (optional)
2. Or comment out logo lines in app.py:

```python
# logo = Image.open("logo.png")  # ← Comment out if missing
```

### ❌ Issue: Streamlit app won't start

**Cause**: Port 8501 already in use or dependency issue  
**Solution**:
```bash
# Kill process on port 8501
# Windows: netstat -ano | findstr :8501
# macOS/Linux: lsof -i :8501

# Try alternative port
streamlit run app.py --server.port 8502
```

### ❌ Issue: Slow analysis or timeouts

**Cause**: Network latency or Groq service load  
**Solution**:
1. Check internet connection
2. Reduce image size (compress before upload)
3. Try again in a few moments

### ❌ Issue: Blurry or incomplete analysis

**Cause**: Image quality is poor  
**Solution**:
1. Upload higher resolution image
2. Ensure good lighting
3. Focus on affected area
4. Minimize shadows and glare

---

## Contributing

### How to Contribute

We welcome contributions! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes
4. **Test** thoroughly
5. **Commit** with clear messages (`git commit -m 'Add amazing feature'`)
6. **Push** to your branch (`git push origin feature/amazing-feature`)
7. **Open** a Pull Request

### Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/medhelp-ai.git

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make changes and test
streamlit run app.py
```

### Areas for Contribution

- ✅ Add support for additional image formats
- ✅ Implement image preprocessing/enhancement
- ✅ Add multiple language support
- ✅ Create additional analysis prompt templates
- ✅ Improve UI/UX design
- ✅ Add unit tests
- ✅ Performance optimization
- ✅ Documentation improvements

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to functions
- Include type hints
- Comment complex logic

---

## Disclaimer

### ⚠️ IMPORTANT MEDICAL DISCLAIMER

**MedHelp AI is NOT:**
- A substitute for professional medical diagnosis
- A treatment recommendation tool
- Capable of providing prescriptions
- A source for definitive medical conclusions

**MedHelp AI IS:**
- An informational tool for educational purposes
- A starting point for health discussions with professionals
- An aid to help you prepare for medical consultations
- A tool to understand general health concepts

### Liability

The creators and operators of MedHelp AI:
- Make no warranties about accuracy or completeness
- Are not liable for medical decisions made using this tool
- Strongly recommend professional medical consultation
- Advise users to seek immediate care for emergencies

### Intended Use

This application is intended for:
- 🟢 Educational health awareness
- 🟢 General health understanding
- 🟢 Preparation for medical appointments
- 🟢 Initial symptom assessment

**NOT intended for:**
- 🔴 Replacing physician judgment
- 🔴 Diagnosing serious conditions
- 🔴 Emergency medical decisions
- 🔴 Self-treatment without professional advice

### Emergency Contacts

If you experience a medical emergency:

- 🚑 **US**: Call 911
- 🚑 **UK**: Call 999
- 🚑 **EU**: Call 112
- 🚑 **Other**: Contact local emergency services

---

## Contact & Support

### Get Help

- **Issues & Bugs**: [GitHub Issues](https://github.com/yourusername/medhelp-ai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/medhelp-ai/discussions)
- **Email**: support@medhelp-ai.com (placeholder)

### Project Links

- **Repository**: https://github.com/yourusername/medhelp-ai
- **Groq Docs**: https://console.groq.com/docs
- **Streamlit Docs**: https://docs.streamlit.io

### Acknowledgments

- **Alibaba / Qwen** - Qwen model
- **Groq** - Fast AI model inference API
- **Streamlit** - Web framework

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-03-19 | Initial release with Llama 4 Scout integration (GitHub AI inference) |
| 1.1.0 | 2026-08-21 | Migrated to Groq API with `qwen/qwen3.6-27b` model; updated API key configuration |
| (Planned) 1.2.0 | Q4 2026 | Chat history, multiple image analysis |
| (Planned) 2.0.0 | Q1 2027 | Advanced RAG, specialist models, user accounts |

---

## FAQ

### Q: Is MedHelp AI a replacement for doctors?
**A**: No. This tool is informational only. Always consult qualified healthcare professionals for medical decisions.

### Q: What size images should I upload?
**A**: Recommended 1MB or less. Supported formats: PNG, JPG, JPEG. Higher resolution = better analysis.

### Q: Can I use this for emergency situations?
**A**: No. For emergencies, call emergency services immediately (911, 999, 112).

### Q: How accurate is the analysis?
**A**: The tool provides educated assessments based on visual analysis, but accuracy depends on image quality and complexity. Never rely solely on this tool.

### Q: Will my data be stored?
**A**: Currently, images are processed but not stored locally by the app. However, they are transmitted to Groq's servers for inference.

### Q: Can I modify the prompt?
**A**: Yes! Edit the `prompt` variable in [app.py](app.py) to customize analysis behavior.

### Q: How do I get a Groq API key?
**A**: Sign up at [console.groq.com](https://console.groq.com) and generate an API key from your account dashboard.

---

## Performance Metrics

Typical performance on standard hardware:

| Operation | Time |
|-----------|------|
| Application startup | 2-3 seconds |
| Image upload | <1 second |
| AI analysis | 2-8 seconds (Groq's low-latency inference) |
| Result rendering | <1 second |
| **Total response time** | **3-10 seconds** |

### Factors Affecting Speed

- 🌍 Network connectivity
- 📸 Image size/resolution
- 🖥️ System resources (CPU, RAM)

---

## Security

### API Key Security

✅ **DO:**
- Store your key as the `GROQ_API_KEY` environment variable
- Keep `.env` in `.gitignore` if you use one
- Use environment variables rather than hardcoding
- Rotate keys regularly

❌ **DON'T:**
- Commit API keys to version control
- Share keys publicly
- Hardcode credentials in `app.py`
- Post keys in issues/PRs

### Example `.gitignore`

```
.env
*.pyc
__pycache__/
*.egg-info/
.DS_Store
venv/
```

---

**Built with ❤️ for health awareness and education**