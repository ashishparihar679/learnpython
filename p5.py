# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# val = 1
# for i in range(row):
#     for j in range(col):
#         print(val,end=" ")
#     print()
#     val+=1
#     if val>9 : val = 1

# enter the number of row : 4
# enter the number of col : 3
# 1 1 1 
# 2 2 2 
# 3 3 3 
# 4 4 4 

#==================================================================================================================== 

# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# for i in range(row):
#     val = 1
#     for j in range(col):
#         print(val,end=" ")
#         val+=1
#     print()

# enter the number of row : 4
# enter the number of col : 3
# 1 2 3 
# 1 2 3 
# 1 2 3 
# 1 2 3 

#==================================================================================================================== 

# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# val = 1
# for i in range(row):
#     for j in range(col):
#         print(val,end=" ")
#         val+=1
#         if val>9 : val=1
#     print()

# enter the number of row : 4
# enter the number of col : 4
# 1 2 3 4 
# 5 6 7 8 
# 9 1 2 3 
# 4 5 6 7 


#==================================================================================================================== 

# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# val = 9
# for i in range(row):
#     for j in range(col):
#         print(val,end=" ")
#         val-=1
#         if val<1 : val=9
    # print()

# enter the number of row : 4
# enter the number of col : 4
# 9 8 7 6 
# 5 4 3 2 
# 1 9 8 7 
# 6 5 4 3 

#==================================================================================================================== 

# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# val = row
# if val > 9 : val = 9
# for i in range(row):
#     for j in range(col):
#         print(val,end=" ")
#     print()
#     val -= 1
#     if val <1 : val = 9

# enter the number of row : 4
# enter the number of col : 3
# 4 4 4 
# 3 3 3 
# 2 2 2 
# 1 1 1 

#==================================================================================================================== 


row = int(input("enter the number of row : "))
col = int(input("enter the number of col : "))
for i in range(row):
    val = col
    for j in range(col):
        print(val,end=" ")
        val -= 1
    print()

# enter the number of row : 4
# enter the number of col : 3
# 3 2 1 
# 3 2 1 
# 3 2 1 
# 3 2 1 

#==================================================================================================================== 