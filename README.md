# Student Performance Prediction System

An end-to-end Machine Learning application that predicts student academic performance using student-related information and assessment scores. The project demonstrates a complete ML workflow, from data preparation and model development to integrating predictions into a Flask-based web application.

## Project Overview

The Student Performance Prediction System aims to estimate students' academic performance based on factors such as gender, ethnicity, parental education, lunch type, test preparation, reading scores and writing scores.

The application accepts student information through a web interface, processes the input using a reusable prediction pipeline, and returns a model-generated prediction.

## Key Features

- **Data Processing:** Prepare student data for machine learning.
- **Feature Engineering:** Transform input features into a suitable model representation.
- **ML Prediction Pipeline:** Use reusable custom data and prediction classes.
- **Flask Web Application:** Provide a web interface for submitting student information.
- **Model Integration:** Connect the trained model and preprocessing components with the application.
- **Modular Architecture:** Separate application code, source modules, templates and model artifacts.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Backend | Flask |
| Frontend | HTML, CSS, Jinja2 |
| Development | Jupyter Notebook, Git, GitHub |

## Project Architecture

```text
mlproject/
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│   └── data_analysis.ipynb
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
├── application.py
├── requirements.txt
├── setup.py
└── README.md
```

*Note: This is an illustrative structure. Check your actual files and artifact names before using it as the definitive repository tree.*

## Application Workflow

1. Collect student information through the Flask interface.
2. Convert submitted information into a structured DataFrame.
3. Pass the input to the prediction pipeline.
4. Apply the saved preprocessing and model components.
5. Generate the predicted academic score.
6. Display the prediction on the web page.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rohitrocker/mlproject.git
cd mlproject
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000/
```

## Learning Outcomes

- Understanding end-to-end machine learning workflows.
- Implementing data preprocessing and feature engineering.
- Building reusable ML prediction pipelines.
- Integrating machine learning models with Flask.
- Understanding modular Python project architecture.
- Deploying model predictions through a web interface.

## Future Improvements

- Add comprehensive model evaluation and comparison.
- Introduce cross-validation and hyperparameter tuning.
- Add interactive performance analytics and visualizations.
- Develop REST API endpoints using FastAPI.
- Containerize the application using Docker.
- Deploy the application to a cloud platform.

## Author

**Rohit Singh**

- GitHub: https://github.com/rohitrocker
- LinkedIn: https://linkedin.com/in/rohit-singh-a97


