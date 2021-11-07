"""Title and price code calculator of movie."""


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
