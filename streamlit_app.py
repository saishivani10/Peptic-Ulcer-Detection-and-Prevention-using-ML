import streamlit as st
from collections import Counter

from PEP import build_models, predict_symptoms

# Cache models so they are built once per session
@st.cache_resource(show_spinner=True)
def get_models():
    tree, forest, gnb, symptoms, diseases = build_models(verbose=False)
    return {
        'tree': tree,
        'forest': forest,
        'gnb': gnb,
        'symptoms': symptoms,
        'diseases': diseases,
    }

st.set_page_config(page_title="Peptic Ulcer Detection and Prevention using ML", page_icon="🩺", layout="wide")
st.title("Peptic Ulcer Detection and Prevention using ML")
st.write(
    "Select your symptoms and choose an algorithm to get a predicted condition."
    " This browser app runs the same ML models as the desktop UI."
)

models = get_models()
all_symptoms = models['symptoms']

left, right = st.columns([2, 1])

with left:
    selected = st.multiselect(
        "Select the symptoms you are experiencing:",
        options=all_symptoms,
        format_func=lambda s: s.replace('_', ' '),
    )

with right:
    alg = st.radio(
        "Algorithm",
        ["Auto (recommended)", "tree", "random", "gnb"],
        index=0,
        help="Auto queries all models and does majority voting",
    )
    predict_clicked = st.button("Predict", type="primary")

if predict_clicked:
    if not selected:
        st.info("Please select at least one symptom.")
    else:
        if alg.startswith("Auto"):
            p1 = predict_symptoms(selected, algorithm='tree')
            p2 = predict_symptoms(selected, algorithm='random')
            p3 = predict_symptoms(selected, algorithm='gnb')
            votes = [p for p in (p1, p2, p3) if p]
            if not votes:
                pred = None
            else:
                cnt = Counter(votes)
                pred, cntv = cnt.most_common(1)[0]
                if cntv == 1 and len(set(votes)) > 1:
                    pred = p1
        else:
            pred = predict_symptoms(selected, algorithm=alg)

        if pred:
            st.success(f"Predicted disease: {pred}")
            st.caption(
                "This prediction is for educational purposes only and not a medical diagnosis. "
                "Please consult a licensed clinician."
            )
        else:
            st.error("Could not predict disease for the selected symptoms.")

st.divider()
st.write("Run locally: `streamlit run streamlit_app.py` ")
