class Student: 
# Class Variables 
    institute_name = "PySpiders" 
    location = "BTM"  
    def __init__(self, sid, name, qual, stream, yop, contact, address, gender):     
        self.sid = sid     
        self.name = name     
        self.qual = qual     
        self.stream = stream     
        self.yop = yop     
        self.contact = contact     
        self.address = address     
        self.gender = gender  
        # Instance Method 
    def display(self):     
        print(f"Student ID : {self.sid}")     
        print(f"Student Name : {self.name}")     
        print(f"Qualification : {self.qual}")     
        print(f"Stream : {self.stream}")     
        print(f"Year of Passout : {self.yop}")     
        print(f"Contact Number : {self.contact}")     
        print(f"Address : {self.address}")     
        print(f"Gender : {self.gender}")     
        print(f"Institute Name : {Student.institute_name}")     
        print(f"Location : {Student.location}")                  

            # Object Creation 
s1 = Student('S1', "Charvi", "BE", "CSE", 2025, 9876543210, "Mysore", "F")  
# Calling Instance Method 
s1.display() 
