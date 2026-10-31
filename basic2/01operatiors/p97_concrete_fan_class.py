from p96_abstract_fan_class import Fan

class calling_Fan(Fan):#Concrete class -> Programmer only


    # concrete class -> concrete method -> to give the implementation for abstract method

    def turn_on(self): #functionality
        print("Ceiling fan turned on") #implementation

    def change_speed(self, new_speed):
        print(f"Speed changed from {self.current_speed} to {new_speed}")

    def turn_off(self):
        print("Ceiling fan turned off") #implementation

obj = calling_Fan(2,3)
obj.motor()
obj.turn_on()
obj.change_speed(5)
obj.turn_off()