from .exceptions import AuthenticationError, NotFoundError, SDKError

def handle_http_error(response):
    """Centralized function to handle HTTP errors."""
    if response.status_code == 401:
        raise AuthenticationError()
    elif response.status_code == 404:
        raise NotFoundError("Requested resource not found.")
    elif response.status_code == 500:
        raise SDKError("Internal server error. Please try again later.")
    else:
        raise SDKError(f"An error occurred: {response.text}")
