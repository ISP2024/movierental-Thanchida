# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.
from datetime import datetime
from movie import Movie
from rental import Rental
from customer import Customer
from pricing import RegularPrice, NewRelease, ChildrenPrice


def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air", 2023, ["Drama", "Sports"]),
        Movie("Oppenheimer", 2023, ["Drama", "Biography", "History"]),
        Movie("Frozen", 2013, ["Animation", "Adventure", "Family"]),
        Movie("Bitconned", 2023, ["Thriller", "Crime"]),
        Movie("Particle Fever", 2013, ["Documentary", "Science"])
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days, movie.price_code_for_movie()))
        days = (days + 2) % 5 + 1
    print(customer.statement())
