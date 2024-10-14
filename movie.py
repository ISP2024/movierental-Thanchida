from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class ChildrenPrice(PriceStrategy):

    def get_price(self, days):
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days):
        return 1


class NewRelease(PriceStrategy):

    def get_price(self, days):
        return 3 * days

    def get_rental_points(self, days):
        return days


class RegularPrice(PriceStrategy):

    def get_price(self, days):
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days):
        return 1


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = RegularPrice()
    NEW_RELEASE = NewRelease()
    CHILDRENS = ChildrenPrice()
    
    def __init__(self, title, price_strategy):
        # Initialize a new movie. 
        self.title = title
        self.price_strategy = price_strategy

    def get_price_code(self):
        # get the price code
        return self.price_strategy
    
    def get_title(self):
        return self.title

    def get_price(self, days):
        return self.price_strategy.get_price(days)

    def get_rental_points(self, days):
        return self.price_strategy.get_rental_points(days)
    
    def __str__(self):
        return self.title
