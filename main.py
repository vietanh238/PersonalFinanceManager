MENU_WIDTH = 60
MENU_SYMBOL = "-"
MENU_TITLE = "PERSONAL FINANCE MANAGER"
VALID_CHOICES = {"1", "2", "3", "4"}
transactions = []

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
        show_transactions()

    elif choice == "4":
        print("Goodbye!")
        return False

    return True

def create_income() -> None:
    custom_line('*', 100, 'CREATE INCOME')
    title = input('enter title income: ').strip()
    category = input('enter category income: ').strip()
    amount = input_amount()

    data = {
        'type': 'Income',
        'title': title,
        'category': category,
        'amount': amount
    }

    transactions.append(data)
    print('[SUCCESS] Transaction added successfully.')

def input_amount() -> bool:
    while True:
        amount = input('enter amount income: ')
        try:
            amount = int(amount)
            if amount <= 0:
                print('amount is invalid')
                continue
            return amount
        except Exception as ex:
            print('Error', ex)

def custom_line(symbol: str, width: int, title) -> None:
    print(title.center(width, symbol))

def show_transactions() -> None:
    custom_line('*', 100, 'SHOW TRANSACTIONS')
    if len(transactions) < 1:
        print('No transactions can view')
    else:
        for tran in transactions:
            print_transaction(tran)
            custom_line('-', 100, '')

def print_transaction(transaction) -> None:
    type = transaction.get('type', '')
    title = transaction.get('title', '')
    category = transaction.get('category', '')
    amount = transaction.get('amount', '')
    print('type: ', type)
    print('title: ', title)
    print('category: ', category)
    print(f'amount: {amount:,}')

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