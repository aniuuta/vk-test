from movie_collection.models import Movie, MovieCollection

def main():
    collection = MovieCollection()
    
    # Add movies
    collection.add_movie(Movie("Inception", 2010, "Sci-Fi", "Christopher Nolan", 8.8))
    collection.add_movie(Movie("The Shawshank Redemption", 1994, "Drama", "Frank Darabont", 9.3))
    
    # Search by title
    print("Search by title:")
    print(collection.search_by_title("Inception"))
    
    # Iterate through collection
    print("\nAll movies:")
    for movie in collection:
        print(movie)
    
    # Search by criteria
    print("\nSearch by criteria (year=2010, genre='Sci-Fi'):")
    results = collection.search_by_criteria({"year": 2010, "genre": "Sci-Fi"})
    print(results)

if __name__ == "__main__":
    main()
