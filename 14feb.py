# incapsulation allows for the hiding for the intrnal state and requiring all intraction to occur throuh well defined interfaces this concert help in acheving data
# abstraction ,data hiding and modularity in software design, promoting thus better core maintaince and reducing compexicity

class car:
    def __init__(self,make,model,year):
        self.__make = make  #private attribute
        self.__model = model
        self.__year = year
        self.__is__started = False

    def start_engine(self):
        self.__is_started = True
        print("Engine strated")

    def stop_engine(self):
        self.__is_started = False
        print("Engine strated")

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def is_engine_strarted(self):
        return self.__is_started

my_car = car("Toyota","camy",2020)

print("Make:",my_car.get_make())
print("Model:",my_car.get_model())
print("Year:",my_car.get_year())

#print("Make:",my_car.__make)
my_car.start_engine()
print("Engine started?" ,my_car.is_engine_strarted())
my_car.stop_engine()
print("Engine started?" ,my_car.is_engine_strarted())




