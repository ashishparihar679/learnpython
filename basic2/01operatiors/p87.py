from p86 import Parent

class Child(Parent):
    b=20
    def __init__(self, p,q):
        super().__init__(p)
        self.q=q

        def meth2(self):
            self.meth1()
            print("I AM A PARENT CLASS")
            print(f"a:{Child.b},p:{self.q}")
obj=Child(100,200)
obj.meth1()