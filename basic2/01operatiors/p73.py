# format() method is used to replace placeholders ({}) in a string with specified values and returns a formatted string.

# s="The person name is {} and age is {} and from the place {}"
# print(s.format("king",45,'mysore'))


# s1="The person name is {name} and age is {age} and from the place {place}"
# print(s1.format(name='Queen',age=34,place='banglore'))

# format_map() is a Python string method that fills placeholders ({}) using a dictionary.
s3="{name1} and {name2} are good friends"
map_obj={'name1':'jake','name2':'jill'}
print(s3.format_map(map_obj))