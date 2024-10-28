import requests
from .models import Movie, Quote
from .error_handling import handle_http_error

class MovieService:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def get_movie_by_id(self, movie_id: str):
        url = f"{self.base_url}/movie/{movie_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return Movie.from_json(response.json()["docs"][0])
        except requests.exceptions.HTTPError:
            handle_http_error(response)

    def get_all_movies(self, limit: int = 100, page: int = None, offset: int = None):
        url = f"{self.base_url}/movie"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"limit": limit}
        if page:
            params["page"] = page
        if offset:
            params["offset"] = offset
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return [Movie.from_json(movie) for movie in response.json()["docs"]]
        except requests.exceptions.HTTPError:
            handle_http_error(response)
    
    def get_movie_quotes(self, movie_id: str):
        url = f"{self.base_url}/movie/{movie_id}/quote"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return [Quote.from_json(quote) for quote in response.json()["docs"]]
        except requests.exceptions.HTTPError:
            handle_http_error(response)
