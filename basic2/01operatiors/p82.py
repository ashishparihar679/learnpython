class Cms:
    def __init__(self,password):
        self.__password=password
        # print(self.__password)

    # getter method
    def get_pw(self):
        return self.__password

    # setter method
    def set_pw(self,new_password):
        if len(new_password) == 8:
            self.__password=new_password
            print("PASSWORD CHANGED")
        else:
            print("SUGGEST TO KEEP EXACTLY 8 CHAR PASSWORD")
obj1=Cms("Lion")
print(obj1.get_pw())  
obj1.set_pw('ashish@1')
print(obj1.get_pw())  