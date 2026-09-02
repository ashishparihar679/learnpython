s1={1,78,55,54,56,12}
s2={1,78,58,56,57,12}
s3={1,7,58,6,5,12}
s1.symmetric_difference(s2)
print(s1)

s1.intersection_update(s2)
print(s1)

s1.symmetric_difference_update(s2)
print(s1)