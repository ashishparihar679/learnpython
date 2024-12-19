 # wap to find number vovels in as tring and number consunat and number special char in a string
n="welcome to_the_city_of_lakes"
vowel = "aeiou"
v=0
s_char=0
con = 0
for i in n:
    if vowel in n:
         v = v+1
    elif n in '_':
         s_char = s_char +1 
    else:
         con=con+1
print(f"vovel = {v} special = {s_char} consunant {con}")