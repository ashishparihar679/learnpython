# li=[1,5,5,5,6,97,3,4]
# for i in range(4):
#     for j in range(1,4):
#        if(li[i]==li[j]):
#         li.remove(li[i])
# print(li)

li = [1, 5, 5, 5, 6, 97, 3, 4]

# Banate hain ek fixed size empty list unique values ke liye
unique_list = [0, 0, 0, 0, 0, 0, 0, 0]  # Same size as li
u_index = 0  # unique_list ka current index

for i in range(8):  # kyunki li me 8 elements hain
    found = 0
    for j in range(u_index):  # unique_list me check karo
        if li[i] == unique_list[j]:
            found = 1
            break
    if found == 0:
        unique_list[u_index] = li[i]
        u_index += 1

# Ab print karte hain unique elements
for k in range(u_index):
    print(unique_list[k], end=" ")
