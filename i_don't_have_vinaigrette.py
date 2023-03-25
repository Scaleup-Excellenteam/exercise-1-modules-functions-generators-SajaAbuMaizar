import random
from datetime import datetime, timedelta

# take in the input from the user
start_date_str = input("Enter start date (YYYY-MM-DD): ")
end_date_str = input("Enter end date (YYYY-MM-DD): ")

# convert the types into datetime
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

# calculate the number of days between the two dates
days_between = (end_date - start_date).days

# generate new date
random_days = random.randint(0, days_between)
new_date = start_date + timedelta(days=random_days)

print(f"The new date is: {new_date.strftime('%Y-%m-%d')}")

# check if the new date is on a Monday
if new_date.weekday() == 0:
    print("אין לי ויניגרט!")
