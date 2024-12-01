from sklearn.feature_extraction.text import TfidfVectorizer
import json
import requests

# Baca artikel dari file JSON
with open('data/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

contents = [article['content'] for article in articles]

# Hitung TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(contents)
feature_names = vectorizer.get_feature_names_out()

# Simpan hasil TF-IDF dalam format JSON
tfidf_data = {
    article['title']: dict(zip(feature_names, row))
    for article, row in zip(articles, tfidf_matrix.toarray())
}

# Kirim hasil ke middleware
response = requests.post('http://localhost:5001/save_tfidf', json=tfidf_data)
print(response.json())
