from p94_multiple import Parent1,Parent2,Parent3

class Child(Parent1,Parent2,Parent3):
    a="child class"

    def __init__(self, p,q,r,s):
        # super().__init__(p)
        Parent1.__init__(self,p)
        Parent2.__init__(self,q)
        Parent3.__init__(self,r)
        self.s=s

    def method_c1(self):
            Parent1.method_p1(self)
            self.method_q1()
            self.method_r1()
            print("I AM A CHILD CLASS")
            print(f"Class variable : {Child.a} r:{self.s}")

obj = Child("A","B","C","D")
obj.method_c1()
# obj.method_p1()