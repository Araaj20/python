# method overriding refer to the ablitity ofsubclass to provide specific implementation of a method that is defined in its superclass.
#when a method in a subclass has the same name ,parameter and return type as method in its superclaas , the method in the subclass overrides the method in the superclass
class A:
    def method(self):
        print("Method of claas A")
class B(A):
    def method(self):
        print("Method of class B")
class C(A):
    def method(self):
        print("Method of class C")
class D(B,C):
    pass
d = D()
d.method()



#return use inside the function to exit the function and return a value back to collor it is typically last statement faunction altough u can have multiple return statememnt
#is different part of function


# paass is use null opration in python is used to pacholder when statement is synatiacaly  refer but u dont"t need any action to be ta
polyme
# duck typing is concept in python where the time or claas of an object is less imp than metod is defines
