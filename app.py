
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="SVM Classification",
    page_icon="🔬",
    layout="wide"
)

@st.cache_resource
def load_model():
    return joblib.load("svm_model.pkl")

st.title("🔬 SVM Breast Cancer Classification")
st.write(
    "Educational demonstration of Support Vector Machine "
    "classification using cell measurements."
)

try:
    saved = load_model()
except FileNotFoundError:
    st.error("Model not found. Run: python train_model.py")
    st.stop()

model = saved["model"]
features = saved["features"]
means = saved["feature_means"]
mins = saved["feature_mins"]
maxs = saved["feature_maxs"]

st.info(
    "This application is for educational purposes only. "
    "It is not a medical diagnostic tool."
)

st.subheader("Enter cell measurement values")

# Choose a subset of features for a manageable demo.
selected_features = [
    "mean radius",
    "mean texture",
    "mean perimeter",
    "mean area",
    "mean smoothness"
]

inputs = {}

with st.form("prediction_form"):
    columns = st.columns(2)

    for i, feature in enumerate(selected_features):
        index = features.index(feature)

        with columns[i % 2]:
            inputs[feature] = st.number_input(
                feature.title(),
                min_value=float(mins[feature]),
                max_value=float(maxs[feature]),
                value=float(means[feature]),
                format="%.4f"
            )

    submitted = st.form_submit_button("Predict")

if submitted:
    # The model was trained using all 30 features.
    # Fill remaining features with their training-data means.
    row = dict(means)
    row.update(inputs)

    input_df = pd.DataFrame([row], columns=features)
    prediction = int(model.predict(input_df)[0])

    st.subheader("Prediction Result")

    if prediction == 0:
        st.error("Model prediction: MALIGNANT")
    else:
        st.success("Model prediction: BENIGN")

    st.caption(
        "The other feature values were set to dataset means. "
        "This is a simplified demonstration, not a valid "
        "clinical assessment."
    )