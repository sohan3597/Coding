#data formats 01: Date and time

from datetime import datetime

current_date_time = datetime.now()

print("Current date and time:", current_date_time)

print("Current date:", current_date_time.date())
print("Current time:", current_date_time.time())
print("Current year:", current_date_time.year)
print("Current month:", current_date_time.month)

#timedelta 

from datetime import timedelta

time_delta = timedelta(days=10)
Yesterday = current_date_time - time_delta
print("30 days ago's date and time:", Yesterday)