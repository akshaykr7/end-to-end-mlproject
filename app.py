from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

app = application

# Route for a HOME page

@app.route('/')
def index():
    return render_template('index.html') # search for index.html file in a templates folder

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_data():
    if request.method=='GET':
        return render_template('home.html')
    else:
        