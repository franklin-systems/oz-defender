class RelayException(Exception):
    """Base exception for Relay API errors"""

    pass


class RelayTimeoutError(RelayException):
    """Timeout exception"""

    pass


class RelayUnauthorizedError(RelayException):
    """Unauthorized exception"""

    pass
