#upper
s="PytHon@123"
print(s.upper()) #PYTHON@123
print(s.lower()) #python@123
print(s.swapcase()) #pYThON@123

t="phtH0n !s vEry ea$y "
print(t.title()) #Phth0N !S Very Ea$Y 
print(t.capitalize()) #Phth0N !S  very ea$y
print(t.casefold()) #Phth0N !S  very ea$y
print(t.lower()) #Phth0N !S  very ea$y


p = "Straße"

print(p.lower())
print(p.casefold())

a = "Straße"
b = "STRASSE"

print(a.lower() == b.lower())
print(a.casefold() == b.casefold())