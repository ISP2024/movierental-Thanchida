import unittest
from customer import Customer
from rental import Rental
from movie import Movie
from pricing import NewRelease, RegularPrice, ChildrenPrice


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, ["Adventure", "Drama", "Sci-Fi"])
        self.regular_movie = Movie("Air", 2023, ["Drama", "Sports"])
        self.childrens_movie = Movie("Frozen", 2013, ["Animation", "Adventure", "Family"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2023, ["Drama", "Sports"])
        self.assertEqual("Air", m.title)
        self.assertEqual(2023, m.year)
        self.assertEqual(["Drama", "Sports"], m.genre)

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1,
                        NewRelease())
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5,
                        NewRelease())
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.childrens_movie, 2,
                        ChildrenPrice())
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5,
                        ChildrenPrice())
        self.assertEqual(rental.get_price(), 4.5)
        rental = Rental(self.regular_movie, 1,
                        RegularPrice())
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 5,
                        RegularPrice())
        self.assertEqual(rental.get_price(), 6.5)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 5,
                        NewRelease())
        self.assertEqual(rental.get_rental_points(), 5)
        rental = Rental(self.childrens_movie, 5,
                        ChildrenPrice())
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 5,
                        RegularPrice())
        self.assertEqual(rental.get_rental_points(), 1)

