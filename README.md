# House Price Prediction

**House Price Prediction** is an interactive web application designed to estimate house prices based on features such as area, number of bedrooms, bathrooms, floors, and age of the house using machine learning algorithms like Linear Regression.
## Project Description

1. **Overview**
   - The project utilizes a dataset containing various house features to predict the price of a house.
   - It employs a machine learning model, specifically Linear Regression, to provide predictions based on user input.
   - Users can input house characteristics, and the application returns the estimated price.
     
2. **Technology Stack**
   - **Frontend:** HTML, CSS, JavaScript
   - **Backend:** Flask (Python)
   - **Machine Learning:** Scikit-learn
   - **Data Storage:** Pickle (for model persistence)

## Project Structure

   ```bash
House-Price-Prediction/
│
├── app.py                                      # Main application file
│
├── models/                                     # Directory for saved machine learning models
│   └── house_price_model.pkl                   # Linear Regression model
│
├── static/                                     # Directory for static files
│   ├── css/                                    # CSS styles for the web interface
│   │   └── styles.css                           # Main stylesheet
│   │
│   └── js/                                     # JavaScript files
│       └── app.js                              # JavaScript file for API interaction
│
└── templates/                                   # Directory for HTML templates
        └── index.html                          # Main HTML file for the web interface
```

## Installation Guide

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.x installed
- Pip (Python package manager)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/House-Price-Prediction.git
   cd House-Price-Prediction
2. **Create a Virtual Environment**
    ```bash
    python -m venv .env
3.**Activate the Virtual Environment**
On Windows:
  ```bash
   .env\Scripts\activate
 ```
On macOS/Linux:
  ```bash
    python -m venv .env
 ```
4.**Install Required Packages**
```bash
    pip install Flask scikit-learn flask-cors pandas
```
  OR
```bash
  pip install -r requirements.txt
```
5.**Run the Application**
```bash
    python app.py
```
The application will start on http://127.0.0.1:5000/.


6.**Access the Web Interface Open your web browser and navigate to http://127.0.0.1:5000/. You can now input flower measurements and classify them using the KNN or Logistic Regression models.**

## Usage
1.**Enter the area, number of bedrooms, bathrooms, floors, and age of the house in the input fields.**
2.**Click on "Predict Price" to get the estimated price of the house.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Contributing

We welcome contributions to enhance **SentimentInsight**! If you're interested in contributing, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature-branch
3. **Commit your changes**:
   ```bash
   git commit -m 'Add feature'
   ```
4. **Push to the branch**:
   ```bash
    git push origin feature-branch
   ```
5. **Open a Pull Request**.


