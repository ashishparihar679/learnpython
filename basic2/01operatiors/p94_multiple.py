class Parent1:
    a="parent1"

    def __init__(self,p):
        self.p=p
    def method_p1(self):
        print("I AM A PARENT1 CLASS")
        print(f"Class variable : {Parent1.a} p : {self.p}")
class Parent2:
    a="parent2"

    def __init__(self,q):
        self.q=q
    def method_q1(self):
        print("I AM A PARENT2 CLASS")
        print(f"Class variable : {Parent2.a} p:{self.q}")
class Parent3:
    a="parent3"

    def __init__(self,r):
        self.r=r
    def method_r1(self):
        print("I AM A PARENT3 CLASS")
        print(f"Class variable : {Parent3.a} r:{self.r}")

