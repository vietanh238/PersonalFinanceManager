MENU_WIDTH = 60
MENU_SYMBOL = "-"
MENU_TITLE = "PERSONAL FINANCE MANAGER"

VALID_CHOICES = {"1", "2", "3", "4"}


def show_menu() -> None:
    """Display the main menu."""

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


def get_user_choice() -> str:
    """Get a valid menu option from the user."""

    while True:
        choice = input("Choose an option: ").strip()

        if choice in VALID_CHOICES:
            return choice

        print(f"[ERROR] Invalid selection. Please choose one of: {', '.join(sorted(VALID_CHOICES))}")


def handle_choice(choice: str) -> bool:
    """
    Handle user's menu selection.

    Returns:
        True  -> Continue program
        False -> Exit program
    """

    if choice == "1":
        create_income()

    elif choice == "2":
        print("[INFO] Add Expense selected.")

    elif choice == "3":
        print("[INFO] View Transactions selected.")

    elif choice == "4":
        print("Goodbye!")
        return False

    return True

def create_income() -> None:
    custom_line('*', 100, 'CREATE INCOME')
    while True:
        title = input('enter title income').strip()
        category = input('enter category income').strip()
        amount = input('enter amount income')

def validate_amount(amount)-> bool:
    pass

def custom_line(symbol: str, width: int, title) -> None:
    print(title.center(width, symbol))

def run() -> None:
    """Main program loop."""

    while True:
        show_menu()

        choice = get_user_choice()

        if not handle_choice(choice):
            break


def main() -> None:
    run()


if __name__ == "__main__":
    main()