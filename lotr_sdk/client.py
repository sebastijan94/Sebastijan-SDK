from .movie_service import MovieService
from .quote_service import QuoteService

class Client:
    BASE_URL = "https://the-one-api.dev/v2"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.movie_service = MovieService(api_key, self.BASE_URL)
        self.quote_service = QuoteService(api_key, self.BASE_URL)

    def get_movie_by_id(self, movie_id: str):
        return self.movie_service.get_movie_by_id(movie_id)
    
    def get_quote_by_id(self, quote_id: str):
        return self.quote_service.get_quote_by_id(quote_id)