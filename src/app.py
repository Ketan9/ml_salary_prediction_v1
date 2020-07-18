#creating web app using flask
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle  

#create flask app object
app = Flask(__name__) 

model = pickle.load(open('src/model.pkl', 'rb'))

#this will be my home page
@app.route('/')    
def home():
    return render_template('index.html')  


#this will be my webAPI. 
@app.route('/predict',methods=['POST']) 
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()] 
    final_features = [np.array(int_features)] 
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))
a =1	

if __name__ == "__main__":
    app.run(debug=True)