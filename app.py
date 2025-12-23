from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open("diabetes_model.pkl", "rb"))

# Define prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json(force=True)

        # Convert features to numpy array
        features = np.array([data["features"]])

        # Make prediction
        prediction = model.predict(features)

        # Return prediction as JSON
        return jsonify({"prediction": int(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
