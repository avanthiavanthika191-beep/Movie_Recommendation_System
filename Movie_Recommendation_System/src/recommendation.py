def recommend(movie_name, movies, similarity):
    movie_name = movie_name.lower()

    if movie_name not in movies["title"].str.lower().values:
        print("Movie not found!")
        return

    index = movies[movies["title"].str.lower() == movie_name].index[0]

    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    print("\nTop 5 Recommended Movies:\n")

    for movie in distances[1:6]:
        print(movies.iloc[movie[0]]["title"])