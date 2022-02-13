import json
from typeform import Typeform
from utils import read_question_ids, read_token

ids_to_questions = read_question_ids()
token = read_token()

responses = Typeform(token).responses
result: dict = responses.list('K43EfCnQ')


with open('results.json', 'w+') as f:
    json.dump(result, f, indent=4)

for key in result.keys():
    print(key)