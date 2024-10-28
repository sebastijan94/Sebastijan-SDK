import requests
from .models import Quote
from .error_handling import handle_http_error

class QuoteService:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def get_quote_by_id(self, quote_id: str):
        url = f"{self.base_url}/quote/{quote_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return Quote.from_json(response.json()["docs"][0])
        except requests.exceptions.HTTPError:
            handle_http_error(response)

    def get_all_quotes(self, limit: int = 100, page: int = None, offset: int = None):
        url = f"{self.base_url}/quote"
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
