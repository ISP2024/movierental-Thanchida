import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie
from datetime import datetime


class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        this_year = datetime.now().year
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", this_year, ["Action", "Adventure", "Drama"])
        self.regular_movie = Movie("CitizenFour", 2014, ["Documentary", "Biography", "Thriller"])
        self.childrens_movie = Movie("Frozen", 2013, ["Children"])

    @unittest.skip("No convenient way to test")
    def test_billing():
        # no convenient way to test billing since its buried in the statement() method.
        pass
    
    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_calculate_total_amount(self):
        customer = Customer("Mim")
        customer.rentals = [
            Rental(self.new_movie, 5),
            Rental(self.childrens_movie, 5),
            Rental(self.regular_movie, 5)
        ]
        self.assertEqual(customer.get_total_charge(), 26)

    def test_calculate_rental_points(self):
        customer = Customer("Mim")
        customer.rentals = [
            Rental(self.new_movie, 5),
            Rental(self.childrens_movie, 5),
            Rental(self.regular_movie, 5)
        ]
        self.assertEqual(customer.get_total_rental_points(), 7)




