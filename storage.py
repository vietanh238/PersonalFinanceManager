import json

transactions: list[dict] = []

def save_transaction(transaction: dict) -> None:
    with open("data/transactions.json", "w") as file:
        transactions.append(transaction)
        json.dump(transactions, file, indent=4)

def load_transactions() -> None:
    with open("data/transactions.json", "r") as file:
        try:
            data = json.load(file)
            transactions.clear()
            transactions.extend(data)
        except json.JSONDecodeError as ex:
            print(ex)