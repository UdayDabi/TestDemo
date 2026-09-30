def readfile():
    file = open("C:/Users/udayd/OneDrive/Desktop/hello.txt", 'r')
    text = file.read()
    print(text)
    file.close()


readfile()
