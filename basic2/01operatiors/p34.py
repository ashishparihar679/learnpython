l=0
while(True):
    n=input("entre pass : ")
    l=l+1
    if n=='a@123':
        print("CORRECT PASSWORD")
        break
    elif l==3:
        print("PASSWORD LIMIT REACHED")
        break
    else:
        print("INCORRECT PASSWORD")
    
