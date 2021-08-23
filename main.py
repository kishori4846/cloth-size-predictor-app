#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('cloth_size.pkl', 'rb'))


#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')
  


#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])

def predict():
    global x
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    o=round(prediction[0],2)
    
    x=""
    
    if 0.01 <= o <= 2.55:
        x="XXS"
    elif 2.55 <= o <= 3.01:
        x="S"
    elif 3.01 <= o <= 3.55:
        x="M"
    elif 3.55 <= o <= 4.01:
        x="XL"
    elif 4.01 <= o <= 5.55:
        x="XXL"
    elif 5.55 <= o <= 9.01:
        x="XXXL"
    elif 9.01 <= o <= 10.01:
        x="XXXXL"
    elif 10.01 <= o <= 12.01:
        x="5XL"

    return render_template('result.html', prediction_text='Your estimated clothing size is : {}'.format(pred_size))
    
if __name__ == "__main__":
    app.run(debug=True)
