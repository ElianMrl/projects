# The Website Version
from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_zip_code():
    response = jsonify({
        'zip_codes': util.get_zip_code()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict', methods=['POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    zipcode = float(request.form['zipcode'])
    bed = int(request.form['bed'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(zipcode,sqft,bed,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)