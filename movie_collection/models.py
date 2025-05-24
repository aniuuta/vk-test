from dataclasses import dataclass
from typing import Dict, Iterator, List, Optional

@dataclass
class Movie:
    title: str
    year: int
    genre: str
    director: str
    rating: float

class MovieCollection:
    def __init__(self):
        self._movies: Dict[str, Movie] = {}
    
    def add_movie(self, movie: Movie) -> bool:
        """Adds a movie to the collection"""
        if movie.title in self._movies:
            return False
        self._movies[movie.title] = movie
        return True
    
    def remove_movie(self, title: str) -> bool:
        """Removes a movie from the collection"""
        if title not in self._movies:
            return False
        del self._movies[title]
        return True
    
    def search_by_title(self, title: str) -> Optional[Movie]:
        """Searches for a movie by title"""
        return self._movies.get(title)
    
    def search_by_criteria(self, criteria: dict) -> List[Movie]:
        """Searches movies by multiple criteria"""
        return [
            movie for movie in self._movies.values()
            if all(
                getattr(movie, key) == value
                for key, value in criteria.items()
            )
        ]
    
    def __iter__(self) -> Iterator[Movie]:
        """Returns iterator for the collection"""
        return iter(self._movies.values())
