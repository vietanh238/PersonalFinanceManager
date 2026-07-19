from constants import (
    TITLE_MAX_LENGTH,
    VALID_CHOICES,
)

from display import print_categories


def get_user_choice() -> str:
    while True:
        choice = input("Choose an option: ").strip()

        if choice in VALID_CHOICES:
            return choice

        print(
            f"[ERROR] Invalid selection. "
            f"Please choose one of: {', '.join(sorted(VALID_CHOICES))}"
        )


def input_title() -> str:
    while True:
        title = input("Enter title: ").strip()

        if not title:
            print("[ERROR] Title cannot be empty.")
            continue

        if len(title) > TITLE_MAX_LENGTH:
            print(f"[ERROR] Maximum length is {TITLE_MAX_LENGTH} characters.")
            continue

        return title


def input_amount() -> int:
    while True:
        amount = input("Enter amount: ").strip()

        try:
            amount = int(amount)

            if amount <= 0:
                print("[ERROR] Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("[ERROR] Please enter a valid number.")


def choose_category(
    categories: tuple[str, ...],
) -> str:

    print_categories(categories)

    while True:
        choice = input("Choose category: ").strip()

        try:
            index = int(choice)

            if not 1 <= index <= len(categories):
                print("[ERROR] Invalid category.")
                continue

            return categories[index - 1]

        except ValueError:
            print("[ERROR] Please enter a number.")