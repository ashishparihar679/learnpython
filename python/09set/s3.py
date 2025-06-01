# wap to make a crade opration on set
s ={ 0 }
while(True):
    ch=int(input('''
enter 1 for create
enter 2 for read
enter 3 for update
enter 4 for delete
enter 5 for exit
'''))
    
    if(ch==1):
        print("create") 
        n=int(input("enter the number of data :- "))
        for i in range(n):
            print(f"enter the {i+1} data :-")
            data=input("enter the data :- ")
            s.add(data)                                                                        
    elif(ch==2):
        print("THE DATA ARE ")
        print(s)
    elif(ch==3):
        print("update")
        n=int(input("enter the number of data to update :- "))
        for i in range(n):
            print(f"enter the {i+1} data :-")
            data=input("enter the data to update :- ")
            s.discard(data)
    elif(ch==4):
        print("update")
        n=int(input("enter the number of data to delete :- "))
        for i in range(n):
            print(f"enter the {i+1} data :-")
            data=input("enter the data to delete :- ")
            data1=data.index(data)
    elif(ch==5):
        break
    else:
        continue
        