# Version
print("Budget - 0.0.1\n")

# Boolean to indiciate menu running
running = True

# List of menu options
menu_options = [
    "1. Add Transaction",
    "2. Delete Transaction",
    "3. Exit Budget"
]

# Function to print menu options
def print_menu(options):
    print("MAIN MENU")
    for option in options:
        print(option)

# While loop to display menu
while running:
    print_menu(menu_options)

    # Get user input
    choice = input("Select an option: ")

    # Process the choice
    if choice == "1":
        print("Adding a transaction...")
        # Add code to handle adding a transaction here
    elif choice == "2":
        print("Deleting a transaction...")
        # Add code to handle deleting a transaction here
    elif choice == "3":
        print("Exiting Budget...")
        running = False
    else:
        print("Invalid option. Please select a valid option from the menu.")
