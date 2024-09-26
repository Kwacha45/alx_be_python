task=input("Enter the task description:")
priority=input("Enter the task priority (high, medium, low):")
time_bound=input("Is the task time-bound? (yes or no):")

match priority:
    case "high":
        print(f"Task '{task}' is marked as HIGH priority. Complete it as soon as possible!")
    case "medium":
        print(f"Task '{task}' is marked as MEDIUM priority. Make sure to complete it soon.")
    case "low":
        print(f"Task '{task}' is marked as LOW priority. Complete it when you have time.")
    case _:
        print(f"Task '{task}' has an unrecognized priority. Defaulting to low priority.")
if time_bound == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "which can be handled based on your availability."

# Print the final reminder message
print(f"\nReminder: Task '{task}' is a {priority_message} task {time_message}")