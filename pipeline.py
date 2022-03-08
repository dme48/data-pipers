from src.master import MasterData

master = MasterData()

pd_df = master.get_master_data()
print(pd_df)
