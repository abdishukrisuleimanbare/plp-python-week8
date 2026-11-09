
# =====================================================
# PLP WEEK 8 FINAL PROJECT
# PERSONAL MINI-TOOLKIT
# Student: Abdishukri Suleiman Bare
# =====================================================

# This list stores tasks while the program is running.
todo_tasks = []


# -----------------------------------------------------
# TOOL 1: NUMBER GUESSING GAME
# Allows users to guess a secret number until correct.
# -----------------------------------------------------

def number_guessing_game():
    print("\n================================")
    print("       NUMBER GUESSING GAME")
    print("================================")
    print("I have selected a number between 1 and 10.")

    secret_number = 7
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")

            elif guess < secret_number:
                print("Too low! Try a higher number.")

            elif guess > secret_number:
                print("Too high! Try a lower number.")

            else:
                print(f"Congratulations! You guessed {secret_number}.")
                print(f"You completed the game in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")


# -----------------------------------------------------
# TOOL 2: TO-DO LIST MANAGER
# Allows users to add, view and remove tasks.
# -----------------------------------------------------

def todo_list_manager():

    while True:
        print("\n================================")
        print("        TO-DO LIST MANAGER")
        print("================================")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter your new task: ").strip()

            if task:
                todo_tasks.append(task)
                print(f"Success! '{task}' has been added.")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            print("\nYOUR CURRENT TASKS")

            if len(todo_tasks) == 0:
                print("Your to-do list is currently empty.")

            else:
                for index, task in enumerate(todo_tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "3":
            if len(todo_tasks) == 0:
                print("There are no tasks to remove.")

            else:
                print("\nYOUR CURRENT TASKS")

                for index, task in enumerate(todo_tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    task_number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= task_number <= len(todo_tasks):
                        removed_task = todo_tasks.pop(task_number - 1)
                        print(f"'{removed_task}' was removed successfully.")

                    else:
                        print("Invalid task number. Please try again.")

                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid option! Please choose between 1 and 4.")


# -----------------------------------------------------
# TOOL 3: SIMPLE CALCULATOR
# Performs basic arithmetic operations.
# -----------------------------------------------------

def simple_calculator():

    print("\n================================")
    print("         SIMPLE CALCULATOR")
    print("================================")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = first_number + second_number
            print(f"Result: {first_number} + {second_number} = {result}")

        elif operation == "2":
            result = first_number - second_number
            print(f"Result: {first_number} - {second_number} = {result}")

        elif operation == "3":
            result = first_number * second_number
            print(f"Result: {first_number} * {second_number} = {result}")

        elif operation == "4":
            if second_number == 0:
                print("Error: Division by zero is not allowed.")

            else:
                result = first_number / second_number
                print(f"Result: {first_number} / {second_number} = {result}")

        else:
            print("Invalid operation! Please select 1, 2, 3 or 4.")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")


# -----------------------------------------------------
# MAIN PROGRAM: MENU-DRIVEN PERSONAL MINI-TOOLKIT
# Repeats the menu until the user chooses to quit.
# -----------------------------------------------------

def main():

    print("\n========================================")
    print(" WELCOME TO MY PERSONAL MINI-TOOLKIT!")
    print("========================================")
    print("Your everyday collection of useful tools.")

    while True:

        print("\n========================================")
        print("             MAIN MENU")
        print("========================================")
        print("1. Number Guessing Game")
        print("2. To-Do List Manager")
        print("3. Simple Calculator")
        print("4. Quit")
        print("========================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            todo_list_manager()

        elif choice == "3":
            simple_calculator()

        elif choice == "4":
            print("\nThank you for using my Personal Mini-Toolkit!")
            print("Keep learning, keep building. Goodbye!")
            break

        else:
            print(
                f"Sorry, '{choice}' is not a valid choice. "
                "Please select a number between 1 and 4."
            )


# Start the program.
if __name__ == "__main__":
    main()
