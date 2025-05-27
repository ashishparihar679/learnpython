Is=[]
while(True):
    print(
    '''
    press 1 for create:
    press 2 for read:
    press 3 for update:
    press 4 for deteate:
    press 5 for exit:
    '''
    )
    ch=int(input("enter the coice :- "))
    if(ch==1):
        n=int(input("enter the number of data :- "))
        for i in range(n):
            print(f"enter the {i+1} data :-")
            data=input("enter the data :- ")
            Is.append(data)
    elif(ch==2):
        print("data ther are")
        print(Is)
    elif(ch==3):
         n=int(input("enter the number of data to update :- "))
         for i in range(n):
            print(f"enter the {i+1} data :-")
            data=input("enter the data to update :- ")
            Is.remove(data)
    # elif(ch==4):
    #      n=int(input("enter the number of data to delete :- "))
    #      for i in range(n):
    #         print(f"enter the {i+1} data :-")
    #         data=input("enter the data to delete :- ")
    #         data1=data.index(data)
    elif(ch==5):
        break
    else:
        continue
    



