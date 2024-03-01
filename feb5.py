#from oops Demo import calculator

from feb2 import calculator



class childimpl(calculator):


    num2=200
    def __init__(self):
        calculator.__init__(self,2,10)

    def getcompletedata(self):
        return self.num2 + self.num + self.summation()

obj=childimpl()
print(obj.getcompletedata())



    #input()
print("Hello world")
print("what is your name")
myname = input()
print("its good to meet you,"+ myname)
print("the length of your name is:")
print(len(myname))
print("wht is your age?")
myage = input()
print("you will be"+ str(int(myage)+1)+"in a year")