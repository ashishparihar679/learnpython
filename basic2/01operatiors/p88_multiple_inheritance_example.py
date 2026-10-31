class Parent:
    def __init__(self,p,r):
        self.p=p
        self.r=r
class Child1(Parent):
    def __init__(self, p, q):
        self.p=p
        self.q=q
class Child2(Parent):
    def __init__(self, p, r):
        super().__init__(p, r)

