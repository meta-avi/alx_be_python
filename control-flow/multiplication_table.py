# multiplication_table.py

# Function to generate the multiplication table
def generate_multiplication_table():
    # Ask the user for a number
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate and print the multiplication table using a for loop
    for i in range(1, 11):
        # Calculate the product
        product = number * i
        # Print the multiplication table in the required format
        print(f"{number} * {i} = {product}")

# Call the function to run the program
if __name__ == "__main__":
    generate_multiplication_table()
