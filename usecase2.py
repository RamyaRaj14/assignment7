#Implement IS-A relationship
class TV:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def getinfo(self):
        print("Model:{} and Brand:{}".format(self.model,self.brand))
    def features(self):
        print("Ultra HD Resolution")
        print("HDR Support")
        print("Wider Colour Space")
        print("10-bit Panel")
        print("HDMI 2.0a Inputs")


class SmartTV(TV):
    def __init__(self,model,brand,screenSize,price,resolution):
        super().__init__(model,brand)
        self.screenSize=screenSize
        self.price=price
        self.resolution=resolution
    def newFeatures(self):
        print("HDCP 2.2 Support")
        print("HEVC Decoding")
        print("4K Streaming Services")
    def tvInfo(self):
        print("Model:",self.model)
        print("Brand:",self.brand)
        print("ScreenSize:",self.screenSize)
        print("Price:",self.price)
        print("Resolution:",self.resolution)



t=SmartTV('Samsung UN55KS9500F','Sony','55 inch','25000','3840X2160')
t.getinfo()
t.features()
t.newFeatures()
t.tvInfo()