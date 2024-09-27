# Prompt user to input a task description
task = input("Enter your task: ")

# Prompt user to input the task's priority (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Prompt user to input if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match case to react based on the priority and prepare the priority level message
match priority:
    case "high":
        priority_message = "high priority"
    case "medium":
        priority_message = "medium priority"
    case "low":
        priority_message = "low priority"
    case _:
        priority_message = "unrecognized priority (defaulting to low)"

# Use an if statement to modify the reminder if the task is time-bound
if time_bound == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "which can be handled based on your availability."

# Print the final reminder message
print(f"Reminder: '{task}' is a {priority_message} task {time_message}")
