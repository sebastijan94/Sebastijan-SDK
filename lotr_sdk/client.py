from .movie_service import MovieService
from .quote_service import QuoteService
from .models import Movie, Quote

class Client:
    """Client for accessing The Lord of the Rings API.

    This class serves as the main interface for interacting with the API, providing methods
    to fetch different types of data.
    """
    BASE_URL = "https://the-one-api.dev/v2"

    def __init__(self, api_key: str):
        """Initialize the Client with the API key.

        Args:
            api_key (str): The API key for accessing the API.
        """
        self.api_key = api_key
        self.movie_service = MovieService(api_key, self.BASE_URL)
        self.quote_service = QuoteService(api_key, self.BASE_URL)

    # Movie-related methods
    def get_movie_by_id(self, movie_id: str) -> Movie:
        """Fetch a movie by its ID.

        Args:
            movie_id (str): The ID of the movie to fetch.

        Returns:
            Movie: An instance of the Movie class representing the requested movie.
        """
        return self.movie_service.get_movie_by_id(movie_id)
    
    def get_all_movies(self, limit: int = 100, page: int = None, offset: int = None) -> list[Movie]:
        """Fetch all movies with optional pagination.

        Args:
            limit (int): The maximum number of movies to return (default is 100).
            page (int): The page number for pagination (optional).
            offset (int): The number of movies to skip for pagination (optional).

        Returns:
            list[Movie]: A list of Movie instances.
        """
        return self.movie_service.get_all_movies(limit, page, offset)
    
    def get_movie_quotes(self, movie_id: str, limit: int = 100, page: int = None, offset: int = None) -> list[Quote]:
        """Fetch all quotes for a specific movie by its ID with optional pagination.

        Args:
            movie_id (str): The ID of the movie for which to fetch quotes.
            limit (int): The maximum number of quotes to return (default is 100).
            page (int): The page number for pagination (optional).
            offset (int): The number of quotes to skip for pagination (optional).

        Returns:
            list[Quote]: A list of Quote instances.
        """
        return self.movie_service.get_movie_quotes(movie_id, limit, page, offset)

    # Quote-related methods
    def get_quote_by_id(self, quote_id: str) -> Quote:
        """Fetch a quote by its ID.

        Args:
            quote_id (str): The ID of the quote to fetch.

        Returns:
            Quote: An instance of the Quote class representing the requested quote.
        """
        return self.quote_service.get_quote_by_id(quote_id)

    def get_all_quotes(self, limit: int = 100, page: int = None, offset: int = None) -> list[Quote]:
        """Fetch all quotes with optional pagination.

        Args:
            limit (int): The maximum number of quotes to return (default is 100).
            page (int): The page number for pagination (optional).
            offset (int): The number of quotes to skip for pagination (optional).

        Returns:
            list[Quote]: A list of Quote instances.
        """
        return self.quote_service.get_all_quotes(limit, page, offset)
    
    # Combined methods
    def get_movie_with_quotes(self, movie_id: str, limit: int = 100, page: int = None, offset: int = None) -> dict:
        """Fetch a movie by its ID along with its quotes with optional pagination.

        Args:
            movie_id (str): The ID of the movie to fetch.
            limit (int): The maximum number of quotes to return (default is 100).
            page (int): The page number for pagination (optional).
            offset (int): The number of quotes to skip for pagination (optional).

        Returns:
            dict: A dictionary containing the movie and its associated quotes.
        """
        movie = self.get_movie_by_id(movie_id)
        quotes = self.get_movie_quotes(movie_id, limit, page, offset)
        return {
            "movie": movie,
            "quotes": quotes
        }
    