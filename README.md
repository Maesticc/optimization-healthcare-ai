# 🚑 Smart Triage & Hospital Dispatch System

## Overview

Smart Triage & Hospital Dispatch System is an AI-powered healthcare application that assists emergency triage and hospital allocation. The system uses a fine-tuned Natural Language Processing (NLP) model to classify patient risk levels based on symptom descriptions and automatically recommends an appropriate healthcare facility.

The application is built with Streamlit and integrates a Hugging Face Transformer model for symptom classification.

---

## Features

* 🤖 AI-based symptom risk assessment
* 🩺 Patient triage classification
* 🏥 Automated hospital recommendation
* 🚑 Patient dispatch simulation
* 📍 Interactive hospital location map using Folium
* 📊 Hospital capacity monitoring dashboard

---

## Risk Classification

The NLP model predicts one of the following categories:

* **HIGH_RISK**

  * Critical conditions requiring immediate attention.
* **MEDIUM_RISK**

  * Moderate conditions requiring prompt treatment.
* **LOW_RISK**

  * Non-emergency conditions.

---

## Project Structure

```text
optimization-healthcare-ai-main/
│
├── st.py
├── README.md
│
└── finished_triage_model/
    ├── config.json
    ├── model.safetensors
    ├── special_tokens_map.json
    ├── tokenizer.json
    ├── tokenizer_config.json
    ├── training_args.bin
    └── vocab.txt
```

---

## Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* Folium
* Streamlit-Folium

---

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd optimization-healthcare-ai-main
```

Or extract the ZIP file and open the project folder.

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install streamlit transformers torch folium streamlit-folium
```

---

## Running the Application

Open Terminal or Command Prompt and navigate to the project folder:

```bash
cd optimization-healthcare-ai-main
```

Then run:

```bash
streamlit run st.py
```

If you rename the application file, use:

```bash
streamlit run nama_app.py
```

Example:

```bash
streamlit run smart_triage.py
```

After running the command, Streamlit will automatically open the application in your browser.

If it does not open automatically, visit:

```text
http://localhost:8501
```

---

## Important Note

The application loads a locally stored fine-tuned model located in:

```text
finished_triage_model/
```

Make sure this folder remains in the project directory and contains all required model files.

If you encounter a path-related error, verify that the model path in `st.py` correctly points to:

```python
MODEL_PATH = "./finished_triage_model"
```

---

## Usage

1. Enter the patient's name.
2. Describe the patient's symptoms.
3. Click **Assess Patient**.
4. Review the predicted risk level.
5. View the recommended hospital.
6. Confirm dispatch.
7. Monitor hospital capacity status.

---

## Future Improvements

* Real-time hospital data integration
* GPS-based hospital recommendation
* Multi-language symptom support
* Ambulance routing optimization
* Electronic Health Record (EHR) integration

---

## Authors

Developed as an AI-assisted healthcare triage and hospital dispatch project utilizing Natural Language Processing and Machine Learning technologies.
