import pandas as pd
from src.master import MasterData


def force_numerical(df: pd.DataFrame, col_name: str):
    """
    Forces the entries at col. column to be numerical, ignoring errors. 
    """
    df[col_name] = pd.to_numeric(df[col_name], errors="coerce")


master = MasterData()
pd_df = master.get_master_data()

# Changes original data
force_numerical(pd_df, "birth_year")
print(pd_df)
