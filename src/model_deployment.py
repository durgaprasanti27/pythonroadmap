# Model Deployment (Flask) - Phase 4

## Flask API Deployment Basics
```python
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Mock ML model (would be replaced with real model)
def predict(input_data):
    return {'prediction': 'class_1', 'confidence': 0.95}

# Home endpoint
@app.route('/')
def home():
    return jsonify({'status': 'API running'})

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict_endpoint():
    input_data = request.json
    result = predict(input_data)
    result['model_version'] = os.environ.get('MODEL_VERSION', 'v1.0')
    return jsonify(result)

# Health check
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'version': os.environ.get('API_VERSION', '1.0')})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

## Deployment Concepts
- **Heroku/Scalability**: Deploy to cloud platforms with auto-scaling
- **Containerization**: Docker wrapper for app consistency
- **Monitoring**: Track API calls, errors, latency
- **Versioning**: Model/Api version tracking endpoints

## Exercises
1. Wrap ML model from previous phase as REST API
2. Add authentication middleware to API
3. Deploy on Heroku (would normally use CLI steps)

**Goal**: Deploy AI models as production-ready REST APIs