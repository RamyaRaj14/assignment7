#Implement IS-A relationship
class Car:
    def __init__(self,model,brand,color):
        self.model=model
        self.brand=brand
        self.color=color
    def getinfo(self):
        print("Model:{},Brand:{} and Color:{}".format(self.model,self.brand,self.color))
    def start(self):
        print("Car Started")
    def move(self):
        print("Car Moved")
    def stop(self):
        print("Car stopped")

class BMW(Car):
    def __init__(self,model,brand,color):
        super().__init__(model,brand,color)
    def  autoPilot(self):
        print("autoPilot")
    def  autoGear(self):
        print("autoGear")
    def carInfo(self):
        print("Model:",self.model)
        print("Brand:",self.brand)
        print("Color:",self.color)



c=BMW('AC Greyhound', 'AC CARS', 'White')
c.getinfo()
c.start()
c.move()
c.stop()
c.autoPilot()
c.autoGear()
c.carInfo()