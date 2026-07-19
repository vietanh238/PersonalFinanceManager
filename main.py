from constants import (
    EXPENSE_CATEGORIES,
    INCOME_CATEGORIES,
)

from display import (
    show_menu,
    show_transactions,
    custom_line
)

from transaction import add_transaction
from validator import (
    get_user_choice,
    input_title,
    choose_category,
    input_amount
)


def handle_choice(
    choice: str,
) -> bool:

    if choice == "1":
        custom_line("*", 100, f"ADD {"Income".upper()}")
        title = input_title()
        category = choose_category(INCOME_CATEGORIES)
        amount = input_amount()
        add_transaction(
            "Income",
            title,
            category,
            amount
        )
        print("[SUCCESS] Transaction added successfully.")
    elif choice == "2":
        custom_line("*", 100, f"ADD {"Expense".upper()}")
        title = input_title()
        category = choose_category(EXPENSE_CATEGORIES)
        amount = input_amount()
        add_transaction(
            "Expense",
            title,
            category,
            amount
        )
        print("[SUCCESS] Transaction added successfully.")
    elif choice == "3":
        show_transactions()

    elif choice == "4":
        print("Goodbye!")
        return False

    return True


def run() -> None:

    while True:
        show_menu()

        choice = get_user_choice()

        if not handle_choice(choice):
            break


def main() -> None:
    run()


if __name__ == "__main__":
    main()