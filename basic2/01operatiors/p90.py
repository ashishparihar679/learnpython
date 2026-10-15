from p89 import Home_appliance
class washing_machine(Home_appliance):
    Home_appliance_type = "Washing machine"

    def __init__(self, brand,color,price,load_type,capacity,mode ):
        super().__init__(brand,color,price)

        self.load_type=load_type
        self.capacity=capacity
        self.mode=mode
    def details_washing_machine(self):
        super().Details_home_appliance()
        print(f"Home_appliance : {washing_machine.Home_appliance_type}")
        print(f"load_type : {self.load_type}")
        print(f"capacity : {self.capacity}")
        print(f"mode : {self.mode}")
obj = washing_machine("apple",'Blue',12000,'front','7kg','auto')
obj.details_washing_machine()
