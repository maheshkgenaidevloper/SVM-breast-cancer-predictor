# SVM-breast-cancer-predictor
# 🎗️ SVM Breast Cancer Predictor | Machine Learning

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=25&pause=1000&color=FF69B4&center=true&vCenter=true&width=700&lines=Breast+Cancer+Prediction+Using+SVM;Machine+Learning+%7C+Python+%7C+Streamlit;Building+AI+for+Healthcare+Analytics" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Machine%20Learning-SVM-purple?style=for-the-badge" alt="Machine Learning SVM" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Project status" />
</p>

<p align="center">
  <img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="420" alt="Technology animation" />
</p>

## 🧬 Project Overview

**SVM Breast Cancer Predictor** is a machine learning project that uses a Support Vector Machine (SVM) classifier to predict whether a breast tumor sample is classified as **benign or malignant** based on numerical diagnostic features.

The project demonstrates a complete machine learning workflow, including data preprocessing, model training, performance evaluation, and interactive prediction through a Streamlit application.

> ⚠️ **Medical disclaimer:** This project is for educational and demonstration purposes only. It is not a medical diagnostic tool and must not be used to make healthcare decisions.

## ✨ Key Features

- 🎯 Breast tumor classification using Support Vector Machine (SVM).
- 🧹 Data preprocessing and feature scaling.
- 🤖 Model training and prediction.
- 📊 Model evaluation using accuracy, precision, recall, F1-score, and confusion matrix.
- 🖥️ Interactive Streamlit web application.
- 🔍 User-input-based prediction interface.
- 📈 Data exploration and visualization.
- 💾 Saved trained model for reuse.
- 🚀 GitHub-ready project structure.

## 🧠 Machine Learning Workflow

<p align="center">
  <img src="https://mermaid.ink/img/pako:eNpVkE1rwzAMhv9K0NM2tK0dW9h2GHaY7aFjG7sYw0o2aYtY1q3k2H_vKc1t0vP0kP0QmYgkG5j0" width="650" alt="Machine learning workflow" />
</p>

1. Load the breast cancer dataset.
2. Inspect and clean the data.
3. Separate input features and target labels.
4. Split the dataset into training and testing sets.
5. Scale numerical features where required.
6. Train the SVM classification model.
7. Evaluate model performance.
8. Save the trained model.
9. Launch the Streamlit application.

## 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,sklearn" alt="Python and machine learning" />
  <img src="https://skillicons.dev/icons?i=vscode,github" alt="VS Code and GitHub" />
</p>

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading and manipulation |
| NumPy | Numerical computations |
| Scikit-learn | SVM model, preprocessing, and evaluation |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Streamlit | Interactive web application |
| Joblib | Saving and loading the trained model |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
SVM-Breast-Cancer-Predictor/
│
├── app.py                  # Streamlit web application
├── train_model.py          # Model training and evaluation
├── breast_cancer.csv       # Dataset, if included in your project
├── requirements.txt        # Required Python libraries
├── README.md               # Project documentation
├── .gitignore              # Files excluded from Git
│
└── models/
    └── svm_model.pkl       # Saved model, generated during training
```

*Note: Keep the filenames and folder structure consistent with your actual project files. If your code uses a different dataset filename or model path, update this README accordingly.*

## ⚙️ Installation and Setup

### 1. Clone the repository

Replace `YOUR_GITHUB_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/SVM-Breast-Cancer-Predictor.git
```

### 2. Open the project folder

```bash
cd SVM-Breast-Cancer-Predictor
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Train the model

```bash
python train_model.py
```

This should train the SVM model, display evaluation metrics, and save the model if your training script is configured to do so.

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

Open the local URL shown in your terminal, usually:

```text
http://localhost:8501
```

## 📦 Requirements

Your `requirements.txt` may contain:

```text
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
joblib
```

Install them with:

```bash
pip install -r requirements.txt
```

## 📊 Model Evaluation

The project can evaluate the SVM classifier using:

| Metric | Purpose |
|---|---|
| Accuracy | Overall proportion of correct predictions |
| Precision | How often positive predictions are correct |
| Recall | How many actual positive cases are detected |
| F1-score | Balance between precision and recall |
| Confusion Matrix | Breakdown of correct and incorrect classifications |

**Important:** Do not publish a model accuracy value unless you have obtained it by running your own training
