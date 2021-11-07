"""Title and price code calculator of movie."""
from typing import List
import csv


class Movie:
    """A movie available for rent."""

    def __init__(self, title: str, year: int, genre: List[str]):
        """Initialize a new movie."""
        self._title = title
        self._year = year
        self._genre = genre

    def get_title(self):
        """Get the title."""
        return self._title

    def get_year(self):
        """Get the year the movie was released."""
        return self._year

    def get_genre(self):
        """Get genre for a movie."""
        return self._genre

    def __str__(self):
        """Return title."""
        return self._title


class MovieCatalog:
    """A list of the movie that customer can rent."""

    def __init__(self):
        """Initialize a new movie."""
        self.movie_list = {}
        with open('movies.csv') as file:
            reader = csv.DictReader(file)
        for i in reader:
            self.movie_list[i["title"]] = {
                "#id": i["#id"],
                "year": i["year"],
                "genre": [j for j in i["genres"].split("|")]
            }

    def get_movie(self, title):
        movie = self.movie_list[title]
        return Movie(title, movie["year"], movie["genre"])
