class Rectangle:
    def getdata(self, length, width):
        self.length = length
        self.width = width
    def area_of_rectangle(self):
        self.area = self.length * self.width
    
rectangle = Rectangle()

length = int(input("Enter length : "))
width = int(input("Enter width : "))

rectangle.getdata(length,width)
rectangle.area_of_rectangle()
print("Area of the rectangle : ",rectangle.area)