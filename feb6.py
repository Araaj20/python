    # over _ Riding
class Employee:
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 40
    def displaythenumberofworkinghours(self):
        print(self.numberofworkinghours)
class Trainee(Employee):
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 45
    def resetnumberofworkinhours(self):
        super().setnumberofworkinghours()

employee = Employee()
employee.setnumberofworkinghours()
print("Number of working hours of employee:", end = " ")
employee.displaythenumberofworkinghours()
trainee = Trainee()
trainee.setnumberofworkinghours()
print("Number of working hours  of traine:", end = " ")
trainee.displaythenumberofworkinghours()
trainee.resetnumberofworkinhours()
print("Number of workimg hours has been reset:", end = " ")
trainee.displaythenumberofworkinghours()
