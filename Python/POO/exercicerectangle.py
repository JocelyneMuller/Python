class Rectangle:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color

#j'appelle la méthode calculate area
    def calculate_area(self):
        return self.length * self.width



rectangle = Rectangle(5,3)
rect1 = Rectangle(4,2,"blue")
rect2 = Rectangle(3,1,color="pink")
print(rectangle.length)
rectangle.color = "yellow"
print(rectangle.color)

area = rectangle.calculate_area()
print(f"l'aire du rectangle est de: {area} m2")
