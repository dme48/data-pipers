"""Collection of utility functions for the pipeline"""
import json

def read_question_ids(filename: str = "question_ids.json"):
    """Reads the file (filename) and returns it as a dictionary"""
    with open(filename, "r") as json_file:
        question_ids = json.load(json_file)
    return question_ids


def read_token(filename: str = "token"):
    """Reads the file (filename) and returns it as a string"""
    with open(filename, "r") as token_file:
        token = token_file.read()
    return token.replace("\n", "")
