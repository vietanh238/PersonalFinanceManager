from storage import save_transaction

def create_transaction(
    transaction_type: str,
    title: str,
    category: str,
    amount: int,
) -> dict:
    return {
        "transaction_type": transaction_type,
        "title": title,
        "category": category,
        "amount": amount,
    }


def add_transaction(
    transaction_type: str,
    title: str,
    category: str,
    amount: int
) -> None:
    transaction = create_transaction(
        transaction_type,
        title,
        category,
        amount,
    )

    save_transaction(transaction)

