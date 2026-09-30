def KeyboardToFileCopy():
    file = open("C:/Users/udayd/OneDrive/Desktop/hello.txt", "w")
    text = input('Enter your message = ')

    while (text != "quit"):
        file.write(text)
        file.write("\n")
        text = input('')
    file.close()


KeyboardToFileCopy()