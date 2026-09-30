import datetime

dob = datetime.date(2005, 10, 30)
today = datetime.date.today()

age = today.year - dob.year
#
#
# # Day name of DOB
# day_name = dob.strftime("%a,%b")
#
print("Your age is:", age)
# print("You were born on:", day_name)
