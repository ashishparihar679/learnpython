import camelcase
c=camelcase.CamelCase()
txt="hy railway"
msg=c.hump(txt)
print(msg)