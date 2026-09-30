class Shape:
    def __init__(self, color, borderWidth):
        print("Shape Constructor Called")
        self.color = color
        self.borderWidth = borderWidth

    def getColor(self):
        return self.color

    def getBorderWidth(self):
        return self.borderWidth


class Rectangle(Shape):

    def __init__(self, length=0, width=0, color='', borderWidth=0):
        self.length = length
        self.width = width
        super().__init__(color, borderWidth)

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width


r = Rectangle(10, 20, 'red', 100)
print("Rectangle:")
print("Length:", r.getLength())
print("Width:", r.getWidth())
print("Color:", r.getColor())
print("Border Width:", r.getBorderWidth())
