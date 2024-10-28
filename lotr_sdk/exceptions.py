class SDKError(Exception):
    """Base class for all SDK errors."""
    pass

class AuthenticationError(SDKError):
    """Raised when authentication fails."""
    def __init__(self, message="Authentication failed. Check your API key."):
        super().__init__(message)

class NotFoundError(SDKError):
    """Raised when a requested resource is not found."""
    def __init__(self, message="Requested resource not found."):
        super().__init__(message)
