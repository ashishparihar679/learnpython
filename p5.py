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


# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# for i in range(row):
#     val = col
#     for j in range(col):
#         print(val,end=" ")
#         val -= 1
#     print()

# enter the number of row : 4
# enter the number of col : 3
# 3 2 1 
# 3 2 1 
# 3 2 1 
# 3 2 1 

#==================================================================================================================== 

# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# # val = 65
# val = ord('A')
# for i in range(row):
#     for j in range(col):
#         print(chr(val),end=" ")
#     print()
#     val += 1
#     if val > 90 : val = 65

# enter the number of row : 4
# enter the number of col : 3
# A A A 
# B B B 
# C C C 
# D D D 

#==================================================================================================================== 

# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# # val = 65
# for i in range(row):
#     val = ord('A')
#     for j in range(col):
#         print(chr(val),end=" ")
#         val += 1
#         if val > 90 : val = 65
#     print()
# enter the number of row : 10
# enter the number of col : 5
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 

# #==================================================================================================================== 

# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# # val = 65
# val = ord('A')
# for i in range(row):
#     for j in range(col):
#         print(chr(val),end=" ")
#         val += 1
#         if val > 90 : val = 65
#     print()

# enter the number of row : 4
# enter the number of col : 3
# A B C 
# D E F 
# G H I 
# J K L 


#==================================================================================================================== 

# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# # val = 65
# val = ord('A')+row-1
# for i in range(row):
#     for j in range(col):
#         print(chr(val),end=" ")
#         # if val > 90 : val = 65
#     print()
#     val += 1

# enter the number of row : 4
# enter the number of col : 3
# D D D 
# E E E 
# F F F 
# G G G 


#==================================================================================================================== 

# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# # val = 65
# for i in range(row):
#     val = ord('A')+col-1
#     for j in range(col):
#         print(chr(val),end=" ")
#         # if val > 90 : val = 65
#         val -= 1    
#     print()

# enter the number of row : 3
# enter the number of col : 10
# J I H G F E D C B A 
# J I H G F E D C B A 
# J I H G F E D C B A 


#==================================================================================================================== 

# 4
# 4
# 4321
# 4321
# 4321
# 4321

# row = int(input("enter the number of row : "))
# col = int(input("enter the number of col : "))
# for i in range(row):
#     val = row
#     for j in range(col):
#         print(val,end=" ")
#         val -=1
#     print()

# enter the number of row : 4
# enter the number of col : 4
# 4 3 2 1 
# 4 3 2 1 
# 4 3 2 1 
# 4 3 2 1 
    

row = int(input("ENTER THE NUMBER OF ROW : "))
col = int(input("ENTER THE NUMBER OF COL : "))

val =1
for i in range(row):
    for j in range(col):
        if i % 2 == 0:
            print(val,end=" ")
          
        else:
            print("*",end=" ")
    print()
    if i%2 == 0:
        val +=1
# ENTER THE NUMBER OF ROW : 5
# ENTER THE NUMBER OF COL : 4
# 1 1 1 1 
# * * * * 
# 2 2 2 2 
# * * * * 
# 3 3 3 3 


# row = int(input("ENTER THE NUMBER OF ROW : "))
# col = int(input("ENTER THE NUMBER OF COL : "))

# for i in range(row):
#     val =1
#     for j in range(col):
#         if j % 2 == 0:
#             print(val,end=" ")
#             val +=1
#         else:
#             print("*",end=" ")
#     print()
#     # if i%2 == 0:
#     #     val +=1

# ENTER THE NUMBER OF ROW : 4
# ENTER THE NUMBER OF COL : 5
# 1 * 2 * 3 
# 1 * 2 * 3 
# 1 * 2 * 3 
# 1 * 2 * 3 