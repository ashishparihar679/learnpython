# abstacrion
from abc import ABC , abstractmethod

class Fan(ABC): #Abstract Base Class / Parent class -> end user + programmer
    min_speed = 1
    max_speed = 5

    def __init__(self,current_speed,blades):
        self.current_speed = current_speed
        self.blades = blades

    @abstractmethod
    def turn_on(self):
        pass

    # abstract class -> concrete method -> comon implementation for all child class

    def motor(self):
        print("motor start rotating")

    @abstractmethod
    def change_speed(self,new_speed):
        pass

    @abstractmethod
    def turn_off(self):
        pass
