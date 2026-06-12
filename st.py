import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import folium
from streamlit_folium import st_folium



st.set_page_config(
    page_title="Smart Triage",
    page_icon="🚑",
    layout="centered"
)

import os

MODEL_REPO = "./fine-tuned-NLP-RS"
SUBFOLDER = "finished_triage_model"

@st.cache_resource
def load_model():
    MODEL_PATH = os.path.join(MODEL_REPO, SUBFOLDER)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

    return pipeline(
        "text-classification",
        model=model,
        tokenizer=tokenizer
    )


classifier = load_model()



HIGH = "HIGH_RISK"
MEDIUM = "MEDIUM_RISK"
LOW = "LOW_RISK"



class Hospital:
    def __init__(self, name, hospital_class, capacity, ugd_capacity=0, location=(0, 0)):
        self.name = name
        self.hospital_class = hospital_class
        self.capacity = capacity
        self.ugd_capacity = ugd_capacity
        self.current = 0
        self.ugd_current = 0
        self.location = location

    def can_handle(self, risk):
        if self.hospital_class == 1 and risk == HIGH:
            return self.ugd_current < self.ugd_capacity or self.current < self.capacity
        return self.current < self.capacity

    def admit(self, risk):
        if self.hospital_class == 1 and risk == HIGH and self.ugd_current < self.ugd_capacity:
            self.ugd_current += 1
        else:
            self.current += 1



if "hospitals" not in st.session_state:
    st.session_state.hospitals = [
        Hospital("National Referral Hospital", 1, 2, ugd_capacity=1, location=(-6.200, 106.816)),
        Hospital("City Hospital", 2, 2, location=(-6.210, 106.820)),
        Hospital("Community Clinic", 3, 3, location=(-6.220, 106.825)),
    ]

if "patient" not in st.session_state:
    st.session_state.patient = None

if "recommendation" not in st.session_state:
    st.session_state.recommendation = None

if "dispatched" not in st.session_state:
    st.session_state.dispatched = False



def reset_patient():
    st.session_state.patient = None
    st.session_state.recommendation = None
    st.session_state.dispatched = False


def hospital_order(risk, hospitals):
    if risk == HIGH:
        return sorted(hospitals, key=lambda h: h.hospital_class)
    elif risk == MEDIUM:
        return sorted(hospitals, key=lambda h: abs(h.hospital_class - 2))
    else:
        return sorted(hospitals, key=lambda h: -h.hospital_class)



st.markdown(
    """
    <h1 style='text-align: center;'>🚑 Smart Triage & Hospital Dispatch</h1>
    <p style='text-align: center; color: gray;'>
        AI-assisted emergency risk assessment and hospital allocation
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()



if st.session_state.patient is None:

    st.subheader("🧑‍⚕️ Patient Information")

    with st.container(border=True):
        name = st.text_input("Patient Name")
        symptoms = st.text_area(
            "Describe Symptoms",
            placeholder="e.g. chest pain, shortness of breath, unconscious..."
        )

        st.markdown("")

        if st.button("🔍 Assess Patient", use_container_width=True):
            if name and symptoms:
                risk = classifier(symptoms)[0]["label"]
                st.session_state.patient = {"name": name, "risk": risk}

                for h in hospital_order(risk, st.session_state.hospitals):
                    if h.can_handle(risk):
                        st.session_state.recommendation = h
                        break
            else:
                st.warning("Please complete all fields")



elif not st.session_state.dispatched:

    p = st.session_state.patient
    h = st.session_state.recommendation

    st.subheader("📋 Triage Result")

    with st.container(border=True):
        if p["risk"] == HIGH:
            st.error(f"⚠️ Risk Level: **{p['risk']}**")
        elif p["risk"] == MEDIUM:
            st.warning(f"⚠️ Risk Level: **{p['risk']}**")
        else:
            st.success(f"✅ Risk Level: **{p['risk']}**")

        st.markdown(
            f"""
            **🏥 Recommended Hospital**  
            {h.name} (Class {h.hospital_class})
            """
        )

    st.markdown("### Confirm Dispatch")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚑 Dispatch Patient", use_container_width=True):
            with st.spinner("Dispatching patient..."):
                pass
            h.admit(p["risk"])
            st.session_state.dispatched = True
            st.rerun()

    with col2:
        if st.button("↩️ Reassess", use_container_width=True):
            reset_patient()
            st.rerun()



else:
    h = st.session_state.recommendation

    st.success("🚑 Patient Successfully Dispatched")
    st.markdown(f"**🏥 Hospital:** {h.name}")

    with st.container(border=True):
        m = folium.Map(location=h.location, zoom_start=13)
        folium.Marker(h.location, popup=h.name).add_to(m)
        st_folium(m, height=300)

    if st.button("➕ New Patient", use_container_width=True):
        reset_patient()
        st.rerun()



with st.expander("🏨 Hospital Capacity Status"):
    for h in st.session_state.hospitals:
        st.write(
            f"**{h.name}** (Class {h.hospital_class})\n"
            f"- Normal: {h.current}/{h.capacity}\n"
            f"- UGD: {h.ugd_current}/{h.ugd_capacity}"
        )
