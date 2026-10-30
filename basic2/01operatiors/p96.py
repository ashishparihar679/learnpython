# abstacrion
from abc import ABC , abstractmethod

class Fan(ABC): #Abstract Base Class / Parent class -> end user + programmer
    min_speed = 1
    max_speed = 5

    def __init__(self,current_speed,blades):
        


