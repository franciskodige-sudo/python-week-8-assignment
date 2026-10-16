"""A friendly menu-driven personal mini-toolkit."""

import random


def simple_calculator():
    """Calculate the result of a basic arithmetic operation."""
    print("\n--- Simple Calculator ---")
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers and try again.")
        return

    operation = input("Choose an operation (+, -, *, /): ").strip()

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("You cannot divide by zero. Please try again.")
            return
        result = first_number / second_number
    else:
        print(f"Sorry, {operation!r} is not a supported operation.")
        return

    print(f"The answer is {result}.")


def todo_list_tool(tasks):
    """Add, view, and remove items in the shared to-do list."""
    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to the main menu")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("What task would you like to add? ").strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("A task cannot be empty.")
        elif choice == "2":
            if tasks:
                print("Your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("Your to-do list is empty.")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
                continue

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
            try:
                task_number = int(input("Enter the number of the task to remove: "))
                removed_task = tasks.pop(task_number - 1)
                print(f"Removed: {removed_task}")
            except ValueError:
                print("Please enter a whole number from the list.")
            except IndexError:
                print("That task number is not on the list.")
        elif choice == "4":
            print("Returning to the main menu.")
            break
        else:
            print(f"Sorry, {choice!r} is not a to-do list option. Please choose 1-4.")


def number_guessing_game():
    """Let the user guess a randomly selected number from 1 to 10."""
    secret_number = random.randint(1, 10)
    print("\n--- Number Guessing Game ---")
    print("I'm thinking of a number from 1 to 10.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number from 1 to 10.")
            continue

        if guess < 1 or guess > 10:
            print("Your guess must be between 1 and 10.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"That's right! The number was {secret_number}.")
            break


def main():
    """Show the menu and run tools until the user chooses to quit."""
    tasks = []
    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\nChoose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            todo_list_tool(tasks)
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            print("Thanks for using your mini-toolkit. Goodbye!")
            break
        else:
            print(f"Sorry, {choice!r} is not on the menu. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
