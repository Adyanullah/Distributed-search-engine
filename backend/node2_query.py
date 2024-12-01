from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    response = requests.get('http://localhost:5001/get_tfidf')
    tfidf_data = response.json()

    # Cari artikel yang relevan berdasarkan query
    results = []
    for title, tfidf in tfidf_data.items():
        score = sum(tfidf.get(word, 0) for word in query.split())
        if score > 0:
            results.append({"title": title, "score": score})
    
    results = sorted(results, key=lambda x: x['score'], reverse=True)
    return jsonify(results)

if __name__ == '__main__':
    app.run(port=5002)  # Node 2 berjalan di port 5002
