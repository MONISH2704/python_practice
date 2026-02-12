#class
class car:  
    #methods
    def __init__(self, color, type, year):
        self.color=color
        self.type=type
        self.year=year
    def details(self):
        print("-----------------------------")
        print("car color: ",self.color)
        print("car type: ",self.type)
        print("car year: ",self.year)
#objects
car1=car("black","sedan",2025)
car2=car("green","suv",2026)
#calling methods
car1.details()
car2.details()