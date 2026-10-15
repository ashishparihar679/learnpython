class Home_appliance:
    type = 'Home Appliance'

    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
    def Details_home_appliance(self):
        print(f"Type of appliance : {Home_appliance.type}")
        print(f"Brand : {self.brand}")
        print(f"color : {self.color}")
        print(f"price : {self.price}")
        