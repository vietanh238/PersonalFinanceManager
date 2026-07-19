transactions: list[dict] = []

def save_transaction(transaction: dict) -> None:
    transactions.append(transaction)

def load_transactions() -> list:
    file = open("F:\My-projects\Python\PersonalFinanceManager\data")
