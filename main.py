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
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = int(prediction)

    sizemap = { 1:'XXS', 2:'S', 3:'M', 4:"L", 5:"XL", 6:"XXL", 7:"XXXL"}
    pred_size = sizemap.get(output)
    

    return render_template('result.html', prediction_text='Your estimated clothing size is : {}'.format(pred_size))
    
if __name__ == "__main__":
    app.run(debug=True)