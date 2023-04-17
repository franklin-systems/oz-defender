class RelayerException(Exception):
    """Base exception for relayer errors"""
    pass


class RelayerTimeout(RelayerException):
    """Timeout exception"""
    pass
