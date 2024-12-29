# match_case_calculator.py

# Function to perform calculations
def calculate():
    try:
        # Getting input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ").strip()

        # Performing the calculation based on user choice using match-case
        match operation:
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case "*":
                result = num1 * num2
            case "/":
                # Handling division by zero
                if num2 == 0:
                    print("Cannot divide by zero.")
                    return
                result = num1 / num2
            case _:
                # In case of invalid operation input
                print("Invalid operation.")
                return

        # Displaying the result
        print(f"The result is {result}")

    except ValueError:
        # Handling invalid input if user doesn't enter a number
        print("Invalid input. Please enter valid numbers.")


# Calling the function to start the calculator
if __name__ == "__main__":
    calculate()
