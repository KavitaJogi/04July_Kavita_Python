class Circle:
    def radius(self, radius):
        self.radius=radius

    def area_of_circle(self):
        self.area = 3.14 * self.radius * self.radius
        
    def perimeter_of_circle(self):
        self.perimeter = 2 * 3.14 * self.radius
        
circle = Circle()

radius = int(input("Enter radius : "))
circle.radius(radius)

circle.area_of_circle()
circle.perimeter_of_circle()

print("Area of circle : ",circle.area)
print("Perimeter of the circle : ",circle.perimeter)