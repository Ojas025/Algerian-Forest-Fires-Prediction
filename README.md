```markdown
# Algerian Forest Fires Prediction App

This is a Flask web application for predicting the Fire Weather Index (FWI) using a trained Ridge Regression model. The model is based on Algerian forest fire data and utilizes standard machine learning tools for preprocessing and prediction.

---

## Features

- Input environmental parameters through a web form  
- Predict Fire Weather Index using a RidgeCV model  
- Scales data with a pre-trained StandardScaler  
- Simple and responsive UI with TailwindCSS  

---

## Technologies Used

- Python 3.x  
- Flask  
- scikit-learn  
- NumPy, Pandas  
- HTML/CSS (TailwindCSS)  
- Pickle for model serialization  

---

## Project Structure

```

project-root/
│
├── application.py                   # Main Flask application
├── models/
│   ├── ridge_cv.pkl         # Trained ML model
│   └── scaler.pkl           # Pre-fitted StandardScaler
│
├── templates/
│   ├── index.html           # Landing page
│   └── home.html            # Form and prediction display
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

```

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/algerian-fire-predictor.git
   cd algerian-fire-predictor
```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate      # On Windows
   source venv/bin/activate   # On macOS/Linux
   ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. Open your browser and visit: `http://localhost:5000`

---

## Input Parameters (via Web Form)

The following values are required for prediction:

* Temperature
* Relative Humidity (RH)
* Wind Speed (Ws)
* Rain
* FFMC
* DMC
* ISI
* Classes (binary encoded)
* Region (binary encoded)

---

## .gitignore Recommendation

To avoid committing unnecessary files, your `.gitignore` should include:

```
venv/
__pycache__/
*.pyc
*.pkl
.env
```