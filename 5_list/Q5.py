my_list = [1,2,3,1,1,1,3,10,5,8]
print(len(my_list))
my_list.append('Append me!')
print(my_list)

a= [1,2,"cybrom",2.05]
a.append("cybrom")
a.append(80)
print(a)

my_list.append([5,6,8,9])
print(my_list)                                                  

my_list.extend(['wubba', 'lubba', 'dub','dub'])
# my_list.append(['wubba', 'lubba', 'dub','dub'])
print(my_list)
# # print(sorted(my_list))
                    
# # pop off the 0 indexed item
# my_list.pop()
# print(my_list)
my_list.pop(-5)
print(my_list)