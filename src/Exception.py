class Error(Exception):
    """Base class for other exceptions"""
    pass

class SelectionError(Exception):
    """Raised when the user selects an invalid option"""
    pass

class Shape44Error(Error):
    """Raised when the puzzle is not a 4x4 matrix"""
    pass

class NotReachableError(Error):
    """Raised when the puzzle solution is not reachable"""
    pass