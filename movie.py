from dataclasses import dataclass
from typing import Collection


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]
    
    def is_genre(self, genre):
        """Return True if genre match any of the movie's genre"""
        return any(g.lower() == genre.lower() for g in self.genre)
    
    def __str__(self):
        return f"{self.title} ({self.year})"
