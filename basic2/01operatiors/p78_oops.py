class Factory:
    a =100
    def __init__(self,material,zip,pocket):
        print(self)
        self.material=material
        self.zip=zip
        self.pocket=pocket
    # def show()
        # print(self.material,)

reebok=Factory("lether",3,2)
reebok=Factory("gethe",4,1)
print(reebok.material)