days_in_a_week = input("How many days are there in a week:  ")
hours_in_a_day = input("How many hours are there in a day:  ")
for hours in hours_in_a_day:
    hours = int(days_in_a_week) * int(hours_in_a_day)
print(hours)
