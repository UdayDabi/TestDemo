class Shape:
    def __init__(self, color, borderWidth):
        self.color = color
        self.borderWidth = borderWidth

    def getColor(self):
        return self.color

    def getBorderWidth(self):
        return self.borderWidth


s = Shape("red",100)
print("Color", s.getColor())
print("BorderWidth", s.getBorderWidth())

# by Set Get Method
# s.setColor("Blue")
# s.setBorderWidth(10)
# print("Color", s.getColor())         # Blue
# print("BorderWidth", s.getBorderWidth())   # 10
