import json
from os.path import exists
from Class_loop_Bank import Bank_Acc
def save_accounts(data, filename="accounts.json"):
    with open(filename, "w") as file:
        # Convert objects to dictionaries before saving
        serializable_data = {acc_no: vars(acc) for acc_no, acc in data.items()}
        json.dump(serializable_data, file, indent=4)
def load_accounts(filename="accounts.json"):
    if not exists(filename):
        return {}
    with open(filename, "r") as file:
        raw_data = json.load(file)
        loaded_accounts = {}
        for acc_no, acc_data in raw_data.items():
            acc_obj = Bank_Acc()
            acc_obj.__dict__.update(acc_data)
            loaded_accounts[int(acc_no)] = acc_obj
        return loaded_accounts
