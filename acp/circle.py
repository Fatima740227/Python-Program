class Circle():
    def __init__(self, r):
        self.radius = r

    def circle_area(self):
        return 3.14 * self.radius * self.radius

    def circle_perimeter(self):
        return 2 * 3.14 * self.radius

newCircle = Circle(7)
print("Dimension of Circle - Radius :", newCircle.radius)
print("Area of Circle :", newCircle.circle_area())
print("Perimeter of Circle :", newCircle.circle_perimeter())