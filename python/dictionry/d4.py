# wap to make a crade opration on dictionary
d ={ }
while(True):
    ch=int(input('''
enter 1 for create
enter 2 for read
enter 3 for update
enter 4 for delete
enter 5 for exit
'''))
    
    if(ch==1):
        n=int(input("enter the number of data :- "))
        print("create") 
        for i in range(n):
         print(f"enter the {i+1} data :-")
         k=input("enter the keys :- ")
         v=input("enter the valus :- ")
         d[k]=v                                                                        
    elif(ch==2):
        print("THE DATA ARE ")
        print(d)
    elif(ch==3):
        print("update")
        n=int(input("enter the number of data to update :- "))
        for i in range(n):
            print(f"enter the {i+1} data :-")
            data=input("enter the data to update :- ")
            d.update(data)
    elif(ch==4):
        print("delete")
        n=int(input("enter the number of data to delete :- "))
        for i in range(n):
            print(f"enter the {i+1} data :-")
            data=input("enter the data to delete :- ")
            d.pop(data)
    elif(ch==5):
        break
    else:
        continue
        