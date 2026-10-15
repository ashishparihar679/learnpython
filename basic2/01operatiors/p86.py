# WITH USING CONSCRUCTURE
class Parent:
    a=10
    def __init__(self,p):
        self.p=p
    def meth1(self):
        print("I AM A PARENT CLASS")
        print(f"a:{Parent.a},p:{self.p}")