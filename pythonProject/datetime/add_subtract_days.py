import  datetime
today  = datetime.date.today()
future = today + datetime.timedelta(days=7000)
past = today - datetime.timedelta(days=7)
# # #
# # #
print("Today",today)
print(" days later:", future)
print("7 days ago:", past)


