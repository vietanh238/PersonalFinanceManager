from constants import (
    MENU_WIDTH,
    MENU_SYMBOL,
    MENU_TITLE,
)

from storage import transactions


def show_menu() -> None:
    line = MENU_SYMBOL * MENU_WIDTH

    print()
    print(line)
    print(MENU_TITLE.center(MENU_WIDTH))
    print(line)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Exit")
    print(line)


def custom_line(
    symbol: str,
    width: int,
    title: str,
) -> None:
    print(title.center(width, symbol))


def print_categories(
    categories: tuple[str, ...],
) -> None:
    print("Choose a category:")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")


def print_transaction(
    transaction: dict,
) -> None:

    print(f"Type      : {transaction['transaction_type']}")
    print(f"Title     : {transaction['title']}")
    print(f"Category  : {transaction['category']}")
    print(f"Amount    : {transaction['amount']:,}")


def show_transactions() -> None:

    custom_line("*", 100, "SHOW TRANSACTIONS")

    if not transactions:
        print("No transactions found.")
        return

    for transaction in transactions:
        print_transaction(transaction)
        custom_line("-", 100, "")