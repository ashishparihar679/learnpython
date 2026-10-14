class Parent:
    a = 90

    def meth_p(self):
        print("i am a parent class")
        print(Parent.a)


class Child(Parent):
    b = 20

    def meth_c(self):
        self.meth_p()  # calling parent class method inside the child class
        print("i am a child class")
        print(Child.b)


obj_p = Parent()
print(dir(obj_p))  # displays available attributes and methods of the Parent object,
                   # including dunder methods, class variable 'a' and method 'meth_p'
                #    Small correction: dir() does not always return exactly 29 dunder methods. The number of attributes and methods can vary depending on the Python version and class definition.

obj_c = Child()
print(dir(obj_c))  # displays available attributes and methods of the Child object,
                   # including inherited dunder methods, class variables 'a', 'b',
                   # and methods 'meth_p', 'meth_c'

obj_c.meth_c()
# i am a parent class
# 90
# i am a child class
# 20

obj_c.meth_p()  # calling the inherited parent class method using the child class object
# i am a parent class
# 90