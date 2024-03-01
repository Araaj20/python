def helloworld():
    print("welcome to the session")
helloworld()
def greet(name):
    print("Hellow,"+name+"!")
greet("Alice")
# def calculate(length,width):
#     area = length*width
#     print (area)
#     return area
# calculate(25,35)

def calculate(length,width):
    area = length*width
    return area
rectangle_length=5
rectangle_width=3
area_result=calculate(rectangle_length,rectangle_width)
print(f"The area of rectangle is:{area_result}")