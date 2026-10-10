
print("Before exception")
a = 10
b = 0
print("Mid ")
try:
    c = a / b
    print(c)

except Exception as e:
    print("An error occurred:", e)
else:
    print("No exception occurred")
finally:
    print("Finally block executed")
print("After exception")



