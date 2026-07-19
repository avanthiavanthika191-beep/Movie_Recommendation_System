import pandas as pd

def load_data():
    movies = pd.read_csv("dataset/movies.csv")
    ratings = pd.read_csv("dataset/ratings.csv")

    movies.drop_duplicates(inplace=True)
    ratings.drop_duplicates(inplace=True)

    return movies, ratings