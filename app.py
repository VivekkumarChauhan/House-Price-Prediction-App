from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import numpy as np
import os

app = Flask(__name__)

# Check if the model exists; if not, train it
model_filename = 'house_price_model.pkl'

if os.path.exists(model_filename):
    # Load the pre-trained model
    model = joblib.load(model_filename)
else:
    # Load your dataset (update this with your actual dataset path)
    df = pd.read_csv('house_data.csv')

    # Features and target variable
    X = df[['area', 'bedrooms', 'bathrooms', 'floors', 'age']]
    y = df['price']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, model_filename)
    print("Model trained and saved as house_price_model.pkl")

@app.route('/')
def index():
    # Render the HTML template for the home page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array([[data['area'], data['bedrooms'], data['bathrooms'], 
                              data['floors'], data['age']]])
        prediction = model.predict(features)
        return jsonify({'price': prediction[0]})
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': 'Error predicting price. Please try again.'})

if __name__ == '__main__':
    app.run(debug=True)
