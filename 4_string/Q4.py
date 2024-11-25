# function
str1= "cybrom indrapuri"
str2= str1.find("n")
# str2= str1.find("t")
print(str2)

str1= "cybrom indrapuri"
# str1[5] = "d"   value assign nhi kar sakte hai but replace kar sakte h
str2 = str1.replace("indrapuri","mpnagar")
print(str2)

s = "apple , banana, grape"
print(s.split(","))