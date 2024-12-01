from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    response = requests.get(f'http://localhost:5002/search?q={query}')
    results = response.json()
    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    app.run(port=5000)  # Frontend berjalan di port 5000
