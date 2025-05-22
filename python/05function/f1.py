# def myfun():


    # wap to find the number having four factor or not betwwen
    #  two input taking from user and using no return with argument function


def four_factor(n1,n2):
    for i in range(n1,n2+1):
        cnt = 0
        for j in range(1 , i+1):
            if(i%j==0):
                cnt+=1
        if(cnt==4):
            print(i)
n1=int(input("entere the number 1 : - "))
n2=int(input("entere the number 2 : - "))
four_factor(n1,n2)