"""
Script containing the MasterData class and related functions
"""
import pandas as pd
from typeform import fetch_typeform
from survey_monkey import fetch_monkey


class MasterData:
    """
    Class designed to combine the results from the different survey platforms,
    providing the ability to update and return them separately. 
    """

    def __init__(self, config: dict):
        """
        Initializes the MasterData instance by fetching the data from the
        different sources.

        The config dictionary is supposed to contain the filenames used by
        fetch_typeform and fetch_monkey, stored at the keys "typeform_login",
        "typeform_config", "monkey_login" and "monkey_config". 
        """

    def update_typeform(self) -> None:
        """Updates the data corresponding to the Typeform surveys"""

    def update_monkey(self) -> None:
        """Updates the data corresponding to the Survey Monkey surveys"""

    def get_typeform_data(self) -> pd.DataFrame:
        """Returns the data corresponding to Typeform as a panads DF"""

    def get_monkey_data(self) -> pd.DataFrame:
        """Returns the data corresponding to Survey Monkey as a panads DF"""

    def get_master_data(self) -> pd.DataFrame:
        """Retuns the combined results from all the sources"""
