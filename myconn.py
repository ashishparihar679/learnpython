import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",   
    port=3306,
    user="root",
    password="1234",
    database="chanchalsir"
)
mycurser=mydb.cursor()

# mycurser.execute("show databases")
# for i in mycurser:
#     print(i)
id=int(input("enter your id"))
name=input("enter your name")
address=input("enter your address")
sql="insert into ib18 (id,name,address) values(%s,%s,%s) "
value=[id,name,address]
mycurser.execute(sql,value)
mydb.commit()
print("inserted")