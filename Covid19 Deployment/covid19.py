from flask import Flask, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

# Define file paths for your datasets
CONFIRMED_FILE_PATH = os.path.join(os.getcwd(), 'datasets', 'time_series_covid19_confirmed_global.csv')
DEATHS_FILE_PATH = os.path.join(os.getcwd(), 'datasets', 'time_series_covid19_deaths_global.csv')
RECOVERED_FILE_PATH = os.path.join(os.getcwd(), 'datasets', 'time_series_covid19_recovered_global.csv')

# Function to load and process data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df.groupby('Country/Region').sum().iloc[:, 4:]

@app.route('/')
def index():
    return render_template('covid19.html')

@app.route('/covid19/confirmed')
def confirmed_cases():
    try:
        confirmed_data = load_data(CONFIRMED_FILE_PATH)
        return jsonify(confirmed_data.to_dict(orient='list'))
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/covid19/deaths')
def death_cases():
    try:
        death_data = load_data(DEATHS_FILE_PATH)
        return jsonify(death_data.to_dict(orient='list'))
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/covid19/recovered')
def recovered_cases():
    try:
        recovered_data = load_data(RECOVERED_FILE_PATH)
        return jsonify(recovered_data.to_dict(orient='list'))
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
