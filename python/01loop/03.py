while(True):
    ch=int(input("\n\nENTER YOUR CHOICE :- \nENTER 1 FOR PRIME NUMBER \nENTER 2 FOR TABLE OF A NUMBER \nENTER 3 FOR BREAK \nENTER 4 FOR ARMSTRAM \nENTER 5 FOR PALINDROM \nENTER 6 FOR fibbonachi series\nenter 7 for find the largest among three numbers \nenter 8 for find the sum of digits of a number   \nenter 9 for Sum of first N natural numbers \n:- "))
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
         break
    elif(ch==4):
        n = int(input("ENTER THE NUMBER :- "))
        p=len(str(n))
        summ=0
        temp=n
        while(n>0):
            r=n%10
            summ= summ +r**p
            n=n//10
        if(summ == temp):
            print("ARMSTRAM")
        else:
            print("NOT ARMSTRAM")
    elif(ch==5):
        n = int(input("ENTER THE NUMBER :- "))
        rev = 0
        temp = n
        while(n>0):
            r = n%10
            rev = rev*10 + r
            n = n // 10
        print(rev)
        if(temp==rev):
            print("NUMBER IS PALINDROME")
        else:
            print("NUMBER IS NOT PALINDROME")
    elif(ch==6):
        n = int(input("ENTER THE NUMBER :- "))
        a=0
        b=1
        i=0
        while(i<n):
            print(a ,end=" ")
            i +=1
            c=a+b
            a = b
            b = c
        
        # Write a Python program to find the largest among three numbers.
    elif(ch==7):
        n1 = int(input("ENTER THE NUMBER 1 :- "))
        n2 = int(input("ENTER THE NUMBER 2 :- "))
        n3 = int(input("ENTER THE NUMBER 3 :- "))
        if(n1>n2 and n1>n3):
            print(f"{n1} IS GREATER THAN {n2} AND {n3}")
        elif(n2>n1 and n2>n3):
            print(f"{n2} IS GREATER THAN {n1} AND {n3}")
        else:
            print(f"{n3} IS GREATER THAN {n1} AND {n2}")

# Write a Python program to find the sum of digits of a number.

    elif(ch==8):
        n = int(input("ENTER THE NUMBER  :- "))
        sum =0
        while(n>0):
            r = n%10
            sum = sum +r
            n= n//10
        print(f"SUM = {sum}")

    elif(ch==9):
        n = int(input("ENTER THE NUMBER  :- "))
        i = 0
        sum =0
        while(i<=n):
            sum = sum + i
            i += 1
        print(sum)


        

    else:
        print("YOUR ENTER WROUNGH INPUT")
        

        
