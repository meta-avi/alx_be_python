def main():
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Customized reminder based on priority and time sensitivity
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Try to complete it soon!")

        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be addressed today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Plan to complete it when possible.")

        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task but requires attention today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

        case _:
            print("Invalid priority entered. Please specify high, medium, or low.")

# Run the program
if __name__ == "__main__":
    main()
