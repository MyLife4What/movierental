"""Demonstrate the movie rental code.

Create a customer with some movies and print a statement.
"""

from movie import MovieCatalog
from rental import Rental
from customer import Customer


def make_movies():
    """Get movie from the catalog."""
    catalog = MovieCatalog()
    movies = [
        catalog.get_movie("Steve Jobs: The Man in the Machine"),
        catalog.get_movie("A Tenant"),
        catalog.get_movie("Deadpool"),
        catalog.get_movie("The Martian"),
        catalog.get_movie("Fifty Shades of Grey")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
