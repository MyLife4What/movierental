from movie import Movie
from rental import Rental, PriceCode


class Customer:
    """A customer who rents movies.

    The customer object holds information about the
    movies rented for the current billing period,
    and can print a statement of his rentals.
    """

    def __init__(self, name: str):
        """Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        """Add rental to rentals list."""
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self):
        """Get the name."""
        return self.name

    def statement(self):
        """Print all the rentals in current period,
        along with total charges and reward points.

        Returns:
            the statement as a String
        """
        total_amount = 0  # total charges
        frequent_renter_points = 0
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"

        for rental in self.rentals:
            amount = rental.get_price()
            frequent_renter_points = rental.get_rental_points()
            #  add detail line to statement
            statement += fmt.format(rental.get_movie().get_title(), rental.get_days_rented(), amount)
            # and accumulate activity
            total_amount += amount
        # footer: summary of charges
        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
            "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)
        return statement


if __name__ == "__main__":
    customer = Customer("Edward Snowden")
    print(customer.statement())
    movie = Movie("Weathering With You", 2020, ["Animation", "Drama", "Children"], PriceCode.children)
    customer.add_rental(Rental(movie, 2))
    movie = Movie("La La Land", 2016, ["Comedy", "Drama", "Romance"], PriceCode.regular)
    customer.add_rental(Rental(movie, 3))
    print(customer.statement())
