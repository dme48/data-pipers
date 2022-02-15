import json
import pandas as pd
from typeform import Typeform
from utils import read_field_ids, read_token, extract_answers

ids_to_fields = read_field_ids()
token = read_token()

responses = Typeform(token).responses
query_result: dict = responses.list('K43EfCnQ')

answers = extract_answers(query_result, ids_to_fields)

dataframe = pd.DataFrame.from_dict(answers)