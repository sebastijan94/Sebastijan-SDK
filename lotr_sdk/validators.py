def validate_positive_integer(value, name):
    """Validate that the given value is a positive integer."""
    if value is not None and (not isinstance(value, int) or value <= 0):
        raise ValueError(f"{name} must be a positive integer.")

def validate_non_negative_integer(value, name):
    """Validate that the given value is a non-negative integer."""
    if value is not None and (not isinstance(value, int) or value < 0):
        raise ValueError(f"{name} must be a non-negative integer.")
