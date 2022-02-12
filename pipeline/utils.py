"""Collection of utility functions for the pipeline"""

def read_token(filename: str = "token"):
    """Reads the file (filename) and returns it as a string"""
    with open(filename) as token_file:
        token = token_file.read()
    return token