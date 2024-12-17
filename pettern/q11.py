 # wap to find number vovels in as tring and number consunat and number special char in a string
n="welcome_to_the_city_of_lakes"
vowel = "aeiou"
v=0
s_char=0
con = 0
for i in n:
    if i in v:
        v = v+1
    elif i=" "," ":
         s_char = s_char +1 
    else:
        con =con+1