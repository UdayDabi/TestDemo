from datetime import datetime



class Person:
    AVG_AGE = 18  # static constant

    def __init__(self):
        print(" Cons is calliing  ther person class")
        self.__name = None
        self.__dob = None
        self.__address = None

    # Getter and Setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and Setter for dob
    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob  # dob should be datetime object

    # Getter and Setter for address
    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    # Age calculation method
    def get_age(self):
        if self.__dob is None:
            return print("Date of Birth not set, please set it to calculate age.")

        now = datetime.now()
        age = now.year - self.__dob.year
        return age


p = Person()
p.set_name("Alok")
p.set_address("Indore")
p.set_dob(datetime(2005, 10, 30))

print("Name:", p.get_name())
print("Address:", p.get_address())
print("Dob",p.get_dob())
print("My Age ", p.get_age())
print("Daf Age ",Person.AVG_AGE)



# print(Person.AVG_AGE)
# print(p.get_age())
# print("ID",id(p)) #object address print

# p1 = Person()
# p1.set_name("Uday")
# p1.set_address("Indore")
# p1.set_dob(datetime(2000, 5, 15))
#
# print("Name:", p1.get_name())
# print(p1.get_dob())
# print("Address:", p1.get_address())
#


#
# print(Person.__doc__)  # prints the docstring of the Person class
# print(Person.__name__)  # prints the name of the Person class
# print(Person.__bases__)  # prints the base classes of the Person class
# print(Person.__dict__)  # prints the namespace of the Person class
