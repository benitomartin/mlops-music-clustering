from flask import Flask, request, jsonify
import joblib
import pandas as pd
import random  # Import the random module


app = Flask(__name__)

# Load the machine learning model
model = joblib.load('model/best_model.pkl')

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Music App!"


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Extract the features from the JSON request
        popularity = data['popularity']
        acousticness = data['acousticness']
        danceability = data['danceability']
        duration_ms = data['duration_ms'] * 50
        energy = data['energy']
        instrumentalness = data['instrumentalness']
        liveness = data['liveness']
        loudness = data['loudness']
        speechiness = data['speechiness']
        tempo = data['tempo']
        valence = data['valence']

        # Create a DataFrame with the input features
        input_data = pd.DataFrame({
            'popularity': [popularity],
            'acousticness': [acousticness],
            'danceability': [danceability],
            'duration_ms': [duration_ms],
            'energy': [energy],
            'instrumentalness': [instrumentalness],
            'liveness': [liveness],
            'loudness': [loudness],
            'speechiness': [speechiness],
            'tempo': [tempo],
            'valence': [valence]
        })

        # Make predictions using the loaded model
        prediction = model.predict(input_data)

        prediction = int(prediction[0])


        return jsonify({'prediction': prediction})
    except Exception as e:

        return jsonify({'error': str(e)})


if __name__ == '__main__':
    # # For local check
    # app.run(debug=True, host='0.0.0.0', port=8080)

    # For AWS
    app.run(host='0.0.0.0', port=8080)