# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract the second number from the first
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide the first number by the second
# Includes a check to prevent division by zero
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to prompt the user for a number
# Repeats the prompt until a valid float is entered
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main calculator function
def calculator():
    try:
        while True:
            # Display the operation options to the user
            print("Select operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")

            # Prompt the user to select an operation
            choice = input("Enter choice(1/2/3/4): ")

            # Check if the user's choice is valid
            if choice in ['1', '2', '3', '4']:
                # Prompt the user for two numbers using the get_number function
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")

                # Perform the chosen operation and display the result
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")

                # Check if the user wants to exit the calculator
                done = input("Type 'done' to exit or press Enter to continue: ")
                if done.lower() == 'done':
                    break  # Exit the loop and end the script
            else:
                # Inform the user if they entered an invalid choice
                print("Invalid Input. Please choose a valid option.")
    except KeyboardInterrupt:
        # Handle the KeyboardInterrupt exception (e.g., when pressing Ctrl+C)
        print("\nProgram interrupted. Exiting...")

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    # Call the calculator function to start the program
    calculator()
