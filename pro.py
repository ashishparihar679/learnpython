import myonn1
ob1=myonn1.DBCONNECTIONPYTHON()
while(True):
    print('''
    press 1 for insert
    press 2 for display
    press 3 for update
    press 4 for find data using roll
    press 5 for delete
    press 6 for stop
''')
    ch=int(input("enter the number"))
    if(ch==1):
        print("insert")
        rollno=input("enter the rollno")
        name=input("enter the name")
        address=input("enter the address")
        sclass=input("enter the clss")
        ob1.RecordInsert(rollno,name,address,sclass)
        print("insert successfully")
    elif(ch==2):
        print("display")
        ob1.RecordDisplay()
    elif(ch==3):
        print("1")

    elif(ch==4):
        print("4")
        ob1.SearchRecord()
        print("RECORD SEARCH SUCCESSFULLY")
    elif(ch==5):
        ob1.deleteRecord()
        print("RECORD DELETE SUCCESSFULLY")
        
    elif(ch==6):
        break
    else:
        print("wroun choice")
    
    