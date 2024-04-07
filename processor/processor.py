from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import heapq

app = Flask(__name__)

documents = []

tfidf_vectorizer = TfidfVectorizer()

@app.route('/query', methods=['POST'])
def process_query():
    data = request.json
    query = data.get('query', '')
    k = data.get('top_k', 5)

    query_vector = tfidf_vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()

    top_k_indices = heapq.nlargest(k, range(len(similarity_scores)), similarity_scores.take)
    top_k_results = [{"document": documents[i], "similarity_score": similarity_scores[i]} for i in top_k_indices]

    return jsonify({"results": top_k_results})

if __name__ == '__main__':
    app.run(debug=True)
