import requests
from .models import Movie, Quote
from .error_handling import handle_http_error

class MovieService:
    """Service for accessing movie-related data from The Lord of the Rings API.

    This class provides methods to fetch movie details and related quotes.
    """

    def __init__(self, api_key: str, base_url: str):
        """Initialize the MovieService with the API key and base URL.

        Args:
            api_key (str): The API key for accessing the API.
            base_url (str): The base URL for the API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_movie_by_id(self, movie_id: str) -> Movie:
        """Fetch a movie by its ID.

        Args:
            movie_id (str): The ID of the movie to fetch.

        Returns:
            Movie: An instance of the Movie class representing the requested movie.

        Raises:
            NotFoundError: If the movie with the given ID is not found.
            AuthenticationError: If the provided API key is invalid.
            SDKError: For general errors related to the API call.
        """
        url = f"{self.base_url}/movie/{movie_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return Movie.from_json(response.json()["docs"][0])
        except requests.exceptions.HTTPError:
            handle_http_error(response)

    def get_all_movies(self, limit: int = 100, page: int = None, offset: int = None) -> list[Movie]:
        """Fetch all movies with optional pagination.

        Args:
            limit (int): The maximum number of movies to return (default is 100).
            page (int): The page number for pagination (optional).
            offset (int): The number of movies to skip for pagination (optional).

        Returns:
            list[Movie]: A list of Movie instances.

        Raises:
            AuthenticationError: If the provided API key is invalid.
            SDKError: For general errors related to the API call.
        """
        url = f"{self.base_url}/movie"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"limit": limit}
        if page is not None:
            params["page"] = page
        if offset is not None:
            params["offset"] = offset
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return [Movie.from_json(movie) for movie in response.json()["docs"]]
        except requests.exceptions.HTTPError:
            handle_http_error(response)
    
    def get_movie_quotes(self, movie_id: str, limit: int = 100, page: int = None, offset: int = None) -> list[Quote]:
        """Fetch all quotes for a specific movie by its ID with optional pagination.

        Args:
            movie_id (str): The ID of the movie for which to fetch quotes.
            limit (int): The maximum number of quotes to return (default is 100).
            page (int): The page number for pagination (optional).
            offset (int): The number of quotes to skip for pagination (optional).

        Returns:
            list[Quote]: A list of Quote instances.

        Raises:
            NotFoundError: If the movie with the given ID is not found.
            AuthenticationError: If the provided API key is invalid.
            SDKError: For general errors related to the API call.
        """
        url = f"{self.base_url}/movie/{movie_id}/quote"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"limit": limit}
        if page is not None:
            params["page"] = page
        if offset is not None:
            params["offset"] = offset
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return [Quote.from_json(quote) for quote in response.json()["docs"]]
        except requests.exceptions.HTTPError:
            handle_http_error(response)
