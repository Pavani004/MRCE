from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load your data (replace 'rainfall.csv' with your actual file)
data = pd.read_csv("rainfall.csv")

# Preprocess data (fill nulls, convert to numeric, etc.)
# Example: Fill null values with mean
data = data.fillna(data.mean())

@app.route('/api/summary', methods=['GET'])
def get_summary():
    summary_stats = data.describe()
    return jsonify(summary_stats)

@app.route('/api/correlation', methods=['GET'])
def get_correlation():
    # Example: Calculate correlation matrix
    correlation_matrix = data.corr()
    return jsonify(correlation_matrix)

if __name__ == '__main__':
    app.run(debug=True)
