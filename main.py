# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from pricing import RegularPrice, NewRelease, ChildrenPrice


def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air"),
        Movie("Oppenheimer"),
        Movie("Frozen"),
        Movie("Bitconned"),
        Movie("Particle Fever")
    ]
    return movies


def make_price_code():
    price_code = [NewRelease(), RegularPrice(),
                  ChildrenPrice(), NewRelease(), RegularPrice()]
    return price_code


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    price_code = make_price_code()
    days = 1
    code = 0
    for movie in make_movies():
        customer.add_rental(Rental(movie, days, price_code[code]))
        days = (days + 2) % 5 + 1
        code += 1
    print(customer.statement())
