import pickle
from flask import Flask,jsonify,render_template,url_for,redirect,Response
import pandas as pd 
import numpy as np
app=Flask(__name__)
predict_model=pickle.load(open('house_pred.pkl','rb'))
scaler=pickle.load(open('scaler_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')
if __name__=='__main__':
    app.run(debug=True)