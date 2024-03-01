# oops
# classes=they are user defined bluprint or protoyype
# eg if calc then,sum multiplication and sunstraction will be methods so calsses will consits of method class variable, instance variable,constructor etc
#creation of new object not needed
class calculator:
    num=100
    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("i am called automatically when object is created")
    def getdata(self):
        print("i am now excuting as method in class")


    def summation(self):
            return self.firstnumber + self.secondnumber + calculator.num


# obj = calculator(20,20)
# obj.getdata()
# print(obj.num)
#
# print(obj.summation())
#


#self is used to refernce to current intance of class when u defined method whitin class u must include self as the 1st parameterr in the method defination
#self keyword is mandt ifor ccalling variable name into method constructor name is also __ init__ new keyword  is not required when u create object
