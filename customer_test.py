"""Test case for a customer who rents movies."""
import re
import unittest
from customer import Customer
from movie import Movie
from rental import Rental, PriceCode


class CustomerTest(unittest.TestCase):
    """Tests of the Customer class."""

    def setUp(self):
        """Test fixture contains: c = a customer movies = list of some movies."""
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("A Tenant", 2020, ["Action", "Sci-Fi"], PriceCode.new_release)
        self.regular_movie = Movie("The Martian", 2016, ["Adventure", "Drama", "Sci-Fi"], PriceCode.regular)
        self.children_movie = Movie("Mulan", 2020, ["Action", "Adventure", "Children"], PriceCode.children)

    @unittest.skip("No convenient way to test")
    def test_billing(self):
        # no convenient way to test billing since its buried in the statement() method.
        pass

    def test_statement(self):
        """A test statement."""
        stmt = self.c.statement()
        # visual testing
        print(stmt)
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
