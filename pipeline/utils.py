"""Collection of utility functions for the pipeline"""
import json
from typing import Iterable


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


def extract_answers(query_response: dict, ids_to_fields: dict):
    """
    Extracts the answers from a Typeform formatted dict (single solved form)
    Arguments:
        query_response (dict): Typeform's dict containing all responses
        ids_to_fields (dict): Connects question ids to corresponding fields
    Returns:
        dict containing the (formatted) answers to the form, in the shape of
        {field_a: [answer_a, answer_b, ...],
         field_b: [answer_a, answer_b, ...],...}.
        If no answer was found at some point, then its answer is None, which
        means that every list has the same length.
    """
    fields = [f for f in ids_to_fields.values()]
    final_answers = {f: [] for f in fields}
    for answer_set in query_response["items"]:
        remaining_fields = set(fields)

        for question in answer_set["answers"]:
            field = ids_to_fields[question["field"]["id"]]
            answer = format_answer(question)
            final_answers[field].append(answer)
            remaining_fields.discard(field)
        for field in remaining_fields:
            final_answers[field].append(None)

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
