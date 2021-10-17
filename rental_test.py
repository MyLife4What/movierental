"""Testcase for renting movie."""
import unittest
from rental import Rental
from movie import Movie, PriceCode


class RentalTest(unittest.TestCase):
	"""Customer renting testcase."""

	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.new_release)
		self.regular_movie = Movie("CitizenFour", PriceCode.regular)
		self.children_movie = Movie("Frozen", PriceCode.children)

	def test_movie_attributes(self):
		"""Trivial test to catch refactoring errors or change in API of Movie."""
		m = Movie("CitizenFour", PriceCode.regular)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.regular, m.get_price_code())

	def test_rental_price(self):
		"""Test for pricing a movie by rented day."""
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.regular_movie, 8)
		self.assertEqual(rental.get_price(), 11.0)
		rental = Rental(self.children_movie, 4)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.children_movie, 6)
		self.assertEqual(rental.get_price(), 6.0)

	def test_rental_points(self):
		"""Test for function get rental points."""
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_rental_points(), 5)
		rental = Rental(self.new_movie, 9)
		self.assertEqual(rental.get_rental_points(), 9)
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_rental_points(), 1)
		rental = Rental(self.regular_movie, 3)
		self.assertEqual(rental.get_rental_points(), 1)
		rental = Rental(self.children_movie, 7)
		self.assertEqual(rental.get_rental_points(), 1)
		rental = Rental(self.children_movie, 10)
		self.assertEqual(rental.get_rental_points(), 1)
