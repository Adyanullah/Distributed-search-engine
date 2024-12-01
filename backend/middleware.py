from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

# Simpan hasil TF-IDF ke database.json
@app.route('/save_tfidf', methods=['POST'])
def save_tfidf():
    data = request.get_json()
    with open('backend/database.json', 'w') as f:
        json.dump(data, f)
    return jsonify({"message": "TF-IDF data saved successfully!"})

# Ambil data TF-IDF dari database.json
@app.route('/get_tfidf', methods=['GET'])
def get_tfidf():
    if os.path.exists('backend/database.json'):
        with open('backend/database.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({"message": "No TF-IDF data found!"})

if __name__ == '__main__':
    app.run(port=5001)  # Middleware berjalan di port 5001
