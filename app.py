import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    t = features[1]
    features[1] = features[2]
    features[2] = t
    final_feat = [np.array(features)]
    prediction = model.predict(final_feat)
    ans = round(prediction[0],2)*100000
    return render_template('index.html', prediction_text = "The median house value is : ${0:.0f}".format(ans))

if __name__ == "__main__":
    app.run(debug=True)
