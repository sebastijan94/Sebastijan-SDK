# The Lord of the Rings SDK

A Python SDK for accessing the Lord of the Rings API, allowing developers to easily fetch movie and quote information from the API.

## Features

- Fetch movie details by ID
- Fetch quotes by ID
- Fetch all movies with optional pagination
- Fetch all quotes with optional pagination
- Fetch quotes associated with a specific movie

## Installation 

0. Ensure you are using Python version >= 3.9

1. Install the SDK:

   ```bash
   pip install git+https://github.com/sebastijan94/Sebastijan-SDK.git
   ```

## Usage

Here is a quick example of how to use the SDK:

```python
from lotr_sdk.client import Client

# Initialize the client with your API key
client = Client(api_key="your_api_key_here")

# Fetch a movie by ID
movie = client.get_movie_by_id("5cd95395de30eff6ebccde5b")
print(f"Movie Name: {movie.name}")

# Fetch all movies with pagination
movies = client.get_all_movies(limit=5, page=1)
print(f"Total Movies: {len(movies)}")

# Fetch quotes for a specific movie
quotes = client.get_movie_quotes("5cd95395de30eff6ebccde5b", limit=5)
for quote in quotes:
    print(f"Quote: {quote.dialog}")
```

### Methods

- **get_movie_by_id(movie_id: str)**
- **get_all_movies(limit: int = 100, page: int = None, offset: int = None)**
- **get_quote_by_id(quote_id: str)**
- **get_all_quotes(limit: int = 100, page: int = None, offset: int = None)**
- **get_movie_quotes(movie_id: str, limit: int = 100, page: int = None, offset: int = None)**
- **get_movie_with_quotes(movie_id: str, limit: int = 100, page: int = None, offset: int = None)**

### Error Handling

The SDK raises exceptions for various error scenarios:

- **NotFoundError**: Raised when a requested resource is not found.
- **AuthenticationError**: Raised when the API key is invalid.
- **SDKError**: For general errors related to the API call. (This error will be raised also for invalid IDs, that is how API currently works)

### Testing

0. Ensure you are using Python version >= 3.9

1. Clone the repository:

   ```bash
   git clone https://github.com/sebastijan94/Sebastijan-SDK.git
   cd Sebastijan-SDK
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your API key:

   ```plaintext
   LOTR_API_KEY=api_key
   ```


4. Run:
   ```bash
   pytest tests/test_sdk.py
   ```
