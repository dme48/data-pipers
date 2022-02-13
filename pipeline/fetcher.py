import json
from typeform import Typeform
from utils import read_question_ids, read_token, extract_answers

ids_to_questions = read_question_ids()
token = read_token()

responses = Typeform(token).responses
result: dict = responses.list('K43EfCnQ')

bare_answers = {i: [] for i in range(len(ids_to_questions))}

for response in result["items"]:
    answers = extract_answers(response)
    print(answers)