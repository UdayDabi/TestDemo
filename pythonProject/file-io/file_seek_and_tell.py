file = open("../files/hello.txt", "r")
str_data = file.read(5)  # Read 3 characters
print(str_data)  # Print the read string
print(file.tell())  # Print current file pointer position
file.close()