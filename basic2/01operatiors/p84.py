class Cms:
    def __init__(self,password):
        self.__password=password
        # getter method
    @property
    def pw(self):
        return self.__password
    # setter method 
    @pw.setter
    def pw(self,new_password):
        if len(new_password) == 8:
            self.__password=new_password
        else:
            print("SUGGEST TO KEEP EXACTLY 8 CHAR PASSWORD")
obj=Cms('lion')
print(obj.pw)
obj.pw="king@123"
print(obj.pw)
