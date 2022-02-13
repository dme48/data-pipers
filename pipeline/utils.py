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


def extract_answers(response: dict):
    """
    Extracts the answers from a Typeform formatted dict (single solved form)
    Arguments:
        response (dict): Typeform's dict for a single solved form
    Returns:
        list containing the (formatted) answers to the form
    """
    final_answers = []
    for question in response["answers"]:
        final_answers.append(format_answer(question))
    return final_answers


FORMAT_GUIDE = {
    "text": lambda x: x,
    "boolean": lambda x: x,
    "number": lambda x: float(x),
    "choice": lambda x: x["label"],
    "choices": lambda x: x["labels"]
}


def format_answer(question):
    """
    Extracts the answer from a question and formats it. Accordingly
    to the FORMAT_GUIDE.
    """
    answer_type = question["type"]
    answer = question[answer_type]

    return FORMAT_GUIDE[answer_type](answer)
