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
        # a={}
        n=int(input("enter the number of data :- "))
        # for i in range(n):
        #     print(f"enter the {i+1} data :-")
        #     b=input("enter the keys :- ")
        #     c=input("enter the valus :- ")
        #     a[b]=c
        #     d.update(a)


        # n=int(input("enter the number of update data :- "))
        # print("update") 
        # for i in range(n):
        #      print(f"enter the {i+1} data :-")
        #      k=input("enter the keys :- ")
        #      v=input("enter the valus :- ")
        #      for j in d.keys():
        #         if(j==d.keys()):
        #            d[k]=v 

        # n = int(input("Enter the number of updates: "))
        #     print("Updating existing keys only...")

# Step 3: Loop for updates
        for i in range(n):
             print(f"\nUpdate {i+1}:")
             k = input("Enter key to update: ")
             if k in d:
                 v = input("Enter new value: ")
                 d[k] = v
                 print(f"Updated: {k} = {v}")
    elif(ch==4):
        print("delete")
        # n=int(input("enter the number of data to delete :- "))
        # for i in range(n):
        #     print(f"enter the {i+1} data :-")
        data=input("enter the data to delete :- ")
        d.pop(data)
    elif(ch==5):
        break
    else:
        continue
        