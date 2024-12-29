# Prompt the user for their task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ")

# Prompt if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level entered."

if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"
elif priority.lower() == "low":
    reminder += ". Consider completing it when you have free time."

# Print the reminder
print(reminder)
