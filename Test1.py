class Car():
    
    def __init__(self,num):
        self.hoge=num
        
    def HogeFunction(self):
        print(self.hoge)

car=Car("Corvette")
car.HogeFunction()
car.hoge="Pythonの文って読みにくくない……？"
car.HogeFunction()

