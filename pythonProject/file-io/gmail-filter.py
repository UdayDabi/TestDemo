import re #Regular Expression


def readLine():
    #base_dir = os.path.dirname(__file__)
   # input_path = os.path.join("C:\\Users\\udayd\\OneDrive\\Desktop", "gmail.txt")
    #output_path = os.path.join("C:\\Users\\udayd\\OneDrive\\Desktop", "correct_gmail.txt")

    input_file = open("D://IO//Email.txt", 'r')
    output_file = open("C:\\Users\\udayd\\OneDrive\\Desktop\\correct_gmail.txt", "w")

    for line in input_file:
        if (re.search("@outlook.com", line)):
            output_file.write(line)
            print(line)
    input_file.close()
    output_file.close()


readLine()
