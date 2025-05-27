task=input("Enter your task : ")
priority=input("Priority(high,medium,low): ")
time_bound=input("Is it time-bound?(yes/no): ")
match priority:
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound.lower() == "no":
            print(f"Reminder: '{task}' is a high priority task that should be completed soon!")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed within the next few days")
        elif time_bound.lower() == "no":
            print(f"Reminder: '{task}'is a medium priority task that should be completed soon!")
    case "low":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a low priority task that can be completed when you have time!")
        elif time_bound.lower() == "no":
            print(f"Reminder: '{task}' is a low priority task.Consider completing it when you have free time!")                    
    