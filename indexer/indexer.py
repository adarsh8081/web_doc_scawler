import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec

class Indexer:
    def __init__(self, documents):
        self.documents = documents
        self.tfidf_vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None
        self.word2vec_model = None

    def build_tfidf_index(self):
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.documents)

    def save_tfidf_index(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.tfidf_vectorizer, self.tfidf_matrix), f)

    def calculate_cosine_similarity(self, query):
        query_vector = self.tfidf_vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrix)
        return cosine_similarities.flatten()
