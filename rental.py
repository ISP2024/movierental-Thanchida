import logging


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    
    def __init__(self, movie, days_rented): 
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        if self.movie.get_price(self.days_rented):
            return self.movie.get_price(self.days_rented)
        log = logging.getLogger()
        log.error(
            f"Movie {self.get_movie()} has unrecognized priceCode {self.get_movie().get_price_code()}")

    def get_rental_points(self):
        return self.movie.get_rental_points(self.days_rented)

