"""Title and price code calculator of movie."""
from enum import Enum


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior.

    The types of movies (price_code).
    """

    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    regular = {"price": lambda days: 2.0 if days <= 2 else 2.0 + (1.5 * (days - 2)),
               "frp": lambda days: 1,
               }
    children = {"price": lambda days: 1.5 if days <= 3 else 1.5 + (1.5 * (days - 3)),
                "frp": lambda days: 1,
                }

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days."""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def get_renter_point(self, day_rented):
        """Get renter point."""
        return self.value["frp"](day_rented)


class Movie:
    """A movie available for rent."""

    def __init__(self, title, price_code):
        """Initialize a new movie."""
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        """Get the price code."""
        return self.price_code

    def get_title(self):
        """Get the title."""
        return self.title

    def __str__(self):
        """Return title."""
        return self.title
