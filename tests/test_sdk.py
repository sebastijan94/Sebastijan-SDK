import os
from dotenv import load_dotenv
import pytest
from lotr_sdk.client import Client
from lotr_sdk.models import Movie, Quote
from lotr_sdk.exceptions import AuthenticationError, NotFoundError, SDKError

load_dotenv()

VALID_API_KEY = os.getenv("LOTR_API_KEY") 
INVALID_API_KEY = "invalid_api_key"

client = Client(api_key=VALID_API_KEY)

def test_get_movie_by_id():
    movie = client.get_movie_by_id("5cd95395de30eff6ebccde5b")
    assert isinstance(movie, Movie), "Expected Movie instance"
    assert movie.name == "The Two Towers"

    # check for both NotFoundError and SDKError as the API returns 500 status code for invalid IDs
    with pytest.raises((NotFoundError, SDKError)):
        client.get_movie_by_id("invalid_id")

def test_get_quote_by_id():
    quote = client.get_quote_by_id("5cd96e05de30eff6ebcce9b8")
    assert isinstance(quote, Quote), "Expected Quote instance"

    with pytest.raises((NotFoundError, SDKError)):
        client.get_quote_by_id("invalid_id")

def test_get_all_movies():
    movies_page = client.get_all_movies(limit=2, page=1)
    assert len(movies_page) <= 2, "Expected up to 2 movies per page"

def test_get_all_quotes():
    quotes_page = client.get_all_quotes(limit=2, page=1)
    assert len(quotes_page) <= 2, "Expected up to 2 quotes per page"

def test_get_movie_quotes():
    quotes = client.get_movie_quotes("5cd95395de30eff6ebccde5b", limit=5)
    assert all(isinstance(quote, Quote) for quote in quotes), "Expected list of Quote instances"

    with pytest.raises((NotFoundError, SDKError)):
        client.get_movie_quotes("invalid_id")

def test_get_movie_with_quotes():
    movie_with_quotes = client.get_movie_with_quotes("5cd95395de30eff6ebccde5b", limit=5)
    assert isinstance(movie_with_quotes['movie'], Movie), "Expected a Movie instance"
    assert isinstance(movie_with_quotes['quotes'], list), "Expected a list of Quote instances"
    assert len(movie_with_quotes['quotes']) <= 5, "Expected up to 5 quotes"

    with pytest.raises((NotFoundError, SDKError)):
        client.get_movie_with_quotes("invalid_id")

# Test invalid API key
def test_invalid_api_key():
    client_invalid = Client(api_key=INVALID_API_KEY)

    with pytest.raises(AuthenticationError):
        client_invalid.get_movie_by_id("5cd95395de30eff6ebccde5b")

# Validation tests
def test_validation_offset():
    # Valid input should not raise an error
    client.get_all_movies(offset=0)  # This should pass

def test_validation_limit():
    with pytest.raises(ValueError, match="limit must be a positive integer."):
        client.get_all_movies(limit=-1)

def test_validation_page():
    with pytest.raises(ValueError, match="page must be a positive integer."):
        client.get_all_movies(page=0)


def test_validation_non_negative_offset():
    with pytest.raises(ValueError, match="offset must be a non-negative integer."):
        client.get_all_movies(offset=-1)