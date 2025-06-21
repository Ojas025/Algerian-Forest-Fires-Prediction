from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler 

application = Flask(__name__)
app = application

# Import the models
with open('models/ridge_cv.pkl','rb') as file:
    model = pickle.load(file)

with open('models/scaler.pkl','rb') as file:
    scaler = pickle.load(file)    

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def predict_data():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        form_data = [
            float(request.form.get('Temperature')),
            float(request.form.get('RH')),
            float(request.form.get('Ws')),
            float(request.form.get('Rain')),
            float(request.form.get('FFMC')),
            float(request.form.get('DMC')),
            float(request.form.get('ISI')),
            float(request.form.get('Classes')),
            float(request.form.get('Region')),
        ]
        
        scaled_data = scaler.transform([form_data])
        result = model.predict(scaled_data)[0]
        
        return render_template('home.html',result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')