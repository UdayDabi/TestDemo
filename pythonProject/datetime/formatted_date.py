import  datetime

today =datetime.date.today()
print("Current date:", today)

formated = today.strftime("%d-%m-%y")

print("Formatted date:", formated)