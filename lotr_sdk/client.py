from .movie_service import MovieService
from .quote_service import QuoteService

class Client:
    BASE_URL = "https://the-one-api.dev/v2"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.movie_service = MovieService(api_key, self.BASE_URL)
        self.quote_service = QuoteService(api_key, self.BASE_URL)

    # Movie-related methods
    def get_movie_by_id(self, movie_id: str):
        """Fetch a movie by its ID."""
        return self.movie_service.get_movie_by_id(movie_id)
    
    def get_all_movies(self, limit: int = 100, page: int = None, offset: int = None):
        """Fetch all movies with optional pagination."""
        return self.movie_service.get_all_movies(limit, page, offset)
    
    def get_movie_quotes(self, movie_id: str):
        """Fetch all quotes for a specific movie by its ID."""
        return self.movie_service.get_movie_quotes(movie_id)

    # Quote-related methods
    def get_quote_by_id(self, quote_id: str):
        """Fetch a quote by its ID."""
        return self.quote_service.get_quote_by_id(quote_id)

    def get_all_quotes(self, limit: int = 100, page: int = None, offset: int = None):
        """Fetch all quotes with optional pagination."""
        return self.quote_service.get_all_quotes(limit, page, offset)
