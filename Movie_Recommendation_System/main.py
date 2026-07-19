from src.data_preprocessing import load_data
from src.similarity import calculate_similarity
from src.recommendation import recommend
from src.utils import welcome

def main():
    welcome()

    # Load and preprocess data
    movies, ratings = load_data()

    # Calculate similarity matrix
    similarity = calculate_similarity(movies)

    # Get movie name from user
    movie_name = input("\nEnter a movie name: ")

    # Recommend movies
    recommend(movie_name, movies, similarity)

if __name__ == "__main__":
    main()

movies, ratings = load_data()

similarity = calculate_similarity(movies)

movie = input("Enter a movie name: ")

recommend(movie, movies, similarity)