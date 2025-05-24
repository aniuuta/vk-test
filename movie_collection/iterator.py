from typing import Iterator, List
from .models import Movie

class MovieIterator(Iterator):
    def __init__(self, movies: List[Movie]):
        self._movies = movies
        self._index = 0
    
    def __next__(self) -> Movie:
        if self._index < len(self._movies):
            movie = self._movies[self._index]
            self._index += 1
            return movie
        raise StopIteration
