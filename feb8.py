#Method overloading as understood in lang like java c++ refers ablity to define multiple method with same name but differnt paramerter with the class.however , python does not support method
#overlaiding in the same way that java or c++ does.


# In pyython ,u can only have  one method with a given name in a class.if u define mulitple method with the same name, the last method definition will override the previous ones.
# therefore,method overloading, as comonly understood ,does not exits in python.

class Mathoperations:
    def add(self,a,b):
        return a + b
    def add(self,a,b,c):
        return a + b + c
math_ops = Mathoperations()
result1 = math_ops.add(2,3,4)
print("Result 1:",result1)
result2 = math_ops.add(2,3)