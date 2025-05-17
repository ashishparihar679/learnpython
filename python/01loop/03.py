while(True):
    ch=int(input("ENTER YOUR CHOICE :- "))
    if(ch==1):
        n = int(input("ENTER THE NUMBER :- "))
        i=1
        cnt =0
        while(i<=n):
            if(n%i==0):
                cnt += 1
            i+=1
        if(cnt==2): 
           print("PRIME")
        else:
           print("NOT PRIME")
    elif(ch==2):
        n = int(input("ENTER THE NUMBER :- "))
        i=1
        while(i<=10):
            print(n," * ",i," = ",n*i)
            i+=1
    elif(ch==3):
        # n = int(input("ENTER THE NUMBER :- "))
        # i=1
        # a=-1
        # b=1
        break
    elif:
        n = int(input("ENTER THE NUMBER :- "))
    
    else:
        print("YOUR ENTER WROUNGH INPUT")
        

        