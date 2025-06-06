import datetime
def  display_current_datetime ():
    current_date=datetime.datetime.now()
    print("Current Date and Time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))
def  calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
display_current_datetime()
calculate_future_date()