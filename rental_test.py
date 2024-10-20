import unittest
from rental import Rental
from movie import Movie
from datetime import datetime


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        this_year = datetime.now().year
        self.new_movie = Movie("Dune: Part Two", this_year, ["Adventure", "Drama", "Sci-Fi"])
        self.regular_movie = Movie("Air", 2023, ["Drama", "Sports"])
        self.childrens_movie = Movie("Frozen", 2013, ["Children"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2023, ["Drama", "Sports"])
        self.assertEqual("Air", m.title)
        self.assertEqual(2023, m.year)
        self.assertEqual(["Drama", "Sports"], m.genre)

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.childrens_movie, 2)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_price(), 6.5)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)

