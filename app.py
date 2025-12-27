from flask import Flask, request, jsonify
from feature_engineering import hash_feature

app = Flask(__name__)

@app.route('/')
def health_check():
    return "MLOps App is running", 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data or 'feature' not in data:
            return jsonify({'error': 'Invalid input, "feature" key required'}), 400
        
        feature_value = data['feature']
        hashed_value = hash_feature(feature_value)
        
        return jsonify({
            'original': feature_value,
            'hashed': hashed_value,
            'status': 'success'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
