import json

transactions = [
    {
        "transaction_type": "Income",
        "title": "Salary",
        "category": "Salary",
        "amount": 20000000
    }
]

with open("data/transactions.json", "w") as file:
    json.dump(transactions, file, indent=4)