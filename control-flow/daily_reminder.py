Task=input("Enter the task description:")
Priority=input("Enter the task priority (high, medium, low):")
Time_bound=input("Is the task time-bound? (yes or no):")

match Priority:
    case "high":
        print(f"Task '{Task}' is marked as HIGH priority. Complete it as soon as possible!")
    case "medium":
        print(f"Task '{Task}' is marked as MEDIUM priority. Make sure to complete it soon.")
    case "low":
        print(f"Task '{Task}' is marked as LOW priority. Complete it when you have time.")
    case _:
        print(f"Task '{Task}' has an unrecognized priority. Defaulting to low priority.")
if Time_bound == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "which can be handled based on your availability."

# Print the final reminder message
print(f"\nReminder: Task '{Task}' is a {Priority} task {time_message}")