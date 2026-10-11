class Factory:
    a =100
    def __init__(selfff,material,zip,pocket):
        print(selfff)
        selfff.material=material
        selfff.zip=zip
        selfff.pocket=pocket
    def show(selfff):
        print(selfff.material,selfff.pocket)

reebok=Factory("lether",3,2)
obj=Factory("gethe",4,1)
# print(reebok.material)
obj.show()