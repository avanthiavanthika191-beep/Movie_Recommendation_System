from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(movies):
    movies["genres"] = movies["genres"].fillna("")

    cv = CountVectorizer(stop_words="english")
    matrix = cv.fit_transform(movies["genres"])

    similarity = cosine_similarity(matrix)

    return similarity