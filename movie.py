import csv
from dataclasses import dataclass
from typing import Collection, Optional
from datetime import datetime
from pricing import NewRelease, RegularPrice, ChildrenPrice


class MovieCatalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance._movies = []
            cls._instance._load_movies_from_csv("movies.csv")
        return cls._instance

    def _load_movies_from_csv(self, filename: str):
        """Load movie from a CSV file"""
        try:
            with open(filename, newline='') as csvfile:
                movie_reader = csv.reader(csvfile)
                next(movie_reader)
                for row in movie_reader:
                    if len(row) != 4:
                        row = ','.join([data for data in row])
                    title = row[1]
                    try:
                        year = int(row[2])
                    except ValueError:
                        continue
                    genres = row[3:]
                    movie = Movie(title, year, genres)
                    self._movies.append(movie)
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def get_movie(self, title: str, year: Optional[int] = None):
        """Return a movie by title. Optionally, match the year"""
        for movie in self._movies:
            if movie.title.lower() == title.lower():
                if year is None or movie.year == year:
                    return movie
        return None


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

    def price_code_for_movie(self):
        if self.year == datetime.now().year:
            print('1', self.title)
            return NewRelease()
        elif any(genre.lower() in ['children', 'childrens'] for genre in self.genre):
            print('2', self.title)
            return ChildrenPrice()
        return RegularPrice()
    
    def __str__(self):
        return f"{self.title} ({self.year})"
