from surveymonkey.client import Client
import json


def load_login(filename: str = "login.json"):
    """Reads surveymonkey credentials from filename and returns them as dict"""
    with open(filename, "r") as f:
        login = json.load(f)
    return login

def load_config(filename: str="form_config.json"):
    """
    Loads the config file at filename and returns a tuple containing its two
    dictionaries.
    """
    with open(filename, "r") as f:
        config = json.load(f)
    return (config["question_by_id"], config["choices_by_id"])

def extract_questions(response):
    questions = response["pages"][0]["questions"]
    for question in questions:
        id = question["id"]
        answer = question["answers"]
        print(answer)

if __name__ == "__main__":
    login = load_login()
    config = load_config()

    client = Client(
        client_id=login["client_id"],
        client_secret=login["client_secret"],
        redirect_uri=login["redirect_uri"],
        access_token=login["access_token"])

    all_responses = client.get_survey_response_bulk(login["form_id"])

    for response in all_responses["data"]:
        print(".............................")
        extract_questions(response, config)
        print(".............................")

