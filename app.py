import pickle
from flask import Flask,request,jsonify,url_for,render_template
import numpy 
import pandas

app = Flask(__name__)
model=pickle.load(open('reg_model.pkl', 'rb'))
app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)

    

                      