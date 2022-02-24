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

    def __init__(self, config: dict = None):
        """
        Initializes the MasterData instance by fetching the data from the
        different sources.

        The config dictionary is supposed to contain the filenames used by
        fetch_typeform and fetch_monkey, stored at the keys "typeform_login",
        "typeform_config", "monkey_login" and "monkey_config". 
        """
        self.config = config
        self.typeform_data = None
        self.monkey_data = None
        self.update_all()

    def update_typeform(self) -> None:
        """Updates the data corresponding to the Typeform surveys"""
        if not config:
            self.typeform_data = fetch_typeform()
            return

        login = self.config["typeform_login"]
        config = self.config["typeform_config"]
        self.typeform_data = fetch_typeform(login, config)

    def update_monkey(self) -> None:
        """Updates the data corresponding to the Survey Monkey surveys"""
        if not config:
            self.monkey_data = fetch_monkey()
            return

        login = self.config["monkey_login"]
        config = self.config["monkey_config"]
        self.monkey_data = fetch_monkey(login, config)

    def update_all(self) -> None:
        """Updates the data from every form"""
        self.update_typeform()
        self.update_monkey()

    def get_typeform_data(self) -> pd.DataFrame:
        """Returns the data corresponding to Typeform as a panads DF"""

    def get_monkey_data(self) -> pd.DataFrame:
        """Returns the data corresponding to Survey Monkey as a panads DF"""

    def get_master_data(self) -> pd.DataFrame:
        """Retuns the combined results from all the sources"""
