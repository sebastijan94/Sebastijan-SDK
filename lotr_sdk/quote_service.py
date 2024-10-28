import requests
from .models import Quote
from .error_handling import handle_http_error

class QuoteService:
    """Service for accessing quote-related data from The Lord of the Rings API.

    This class provides methods to fetch quotes and associated details.
    """

    def __init__(self, api_key: str, base_url: str):
        """Initialize the QuoteService with the API key and base URL.

        Args:
            api_key (str): The API key for accessing the API.
            base_url (str): The base URL for the API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_quote_by_id(self, quote_id: str) -> Quote:
        """Fetch a quote by its ID.

        Args:
            quote_id (str): The ID of the quote to fetch.

        Returns:
            Quote: An instance of the Quote class representing the requested quote.

        Raises:
            NotFoundError: If the quote with the given ID is not found.
            AuthenticationError: If the provided API key is invalid.
            SDKError: For general errors related to the API call.
        """
        url = f"{self.base_url}/quote/{quote_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return Quote.from_json(response.json()["docs"][0])
        except requests.exceptions.HTTPError:
            handle_http_error(response)

    def get_all_quotes(self, limit: int = 100, page: int = None, offset: int = None) -> list[Quote]:
        """Fetch all quotes with optional pagination.

        Args:
            limit (int): The maximum number of quotes to return (default is 100).
            page (int): The page number for pagination (optional).
            offset (int): The number of quotes to skip for pagination (optional).

        Returns:
            list[Quote]: A list of Quote instances.

        Raises:
            AuthenticationError: If the provided API key is invalid.
            SDKError: For general errors related to the API call.
        """
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
