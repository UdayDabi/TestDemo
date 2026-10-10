class Addition:
    def sum(self, a, b):
        return a + b;

class Multiplication:
    def multiply(self, a, b):
        return a * b;

class Divide:
    def Divide(self, a, b):
        return a / b;

class test(Addition, Multiplication,Divide):  # derived class inherits both addition and mu,tiplacation base class
   pass


t = test()
print(t.sum(10, 20))
print(t.multiply(10, 20))
print(t.Divide(10, 20))
