#Implement HAS-A relationship
class Memory:
    def __init__(self,internal,secondary,ram):
        self. internal= internal
        self.secondary=secondary
        self.ram=ram
    def getinfo(self):
        print("internal:{},Model:{} and Color:{}".format(self.internal,self.secondary,self.ram))

class  Mobile:
    def __init__(self,model,brand,price,memory):
        self.model=model
        self.brand=brand
        self.price=price
        self.memory=memory
    def mobinfo(self):
        print("Mobile Model:",self.model)
        print("Mobile Brand:",self.brand)
        print("Mobile Price:",self.price)
        print("Mobile Info:",end=" ")
        self.memory.getinfo()

me=Memory("XYZ","abc","4")
m=Mobile('Sony45','sony','15000',me)
m.mobinfo()