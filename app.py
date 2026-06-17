from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/predict")
def predict():

    data = {
        "soil_moisture": "70%",
        "flood_risk": "Medium",
        "water_storage": "80%",
        "recommendation":
        "Build artificial root channels"
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
