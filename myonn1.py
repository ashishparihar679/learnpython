class DBCONNECTIONPYTHON:
    def __init__(self):
        import mysql.connector
        self.mydb=mysql.connector.connect(
            host="localhost",   
            port=3306,
            user="root",
            password="1234",
            database="chanchalsir"
        )
        self.cursor=self.mydb.cursor()
    def RecordInsert(self,rollno,name,address,sclass):
        self.rollno=rollno
        self.name=name
        self.address=address
        self.sclass=sclass
        sql="insert into ib18 (rollno,name,address,sclass) values(%s,%s,%s,%s)"
        value=[self.rollno,self.name,self.address,self.sclass]
        self.cursor.execute(sql,value)
        self.mydb.commit()
# print("inserted")
    def RecordDisplay(self):
        sql="select * from ib18"
        self.cursor.execute(sql)
        mydata=self.cursor.fetchall()
        for i in mydata:
            print(i)
    def RecordUpdate(self):
        rollno=input("enter the roll no for update: ")
        name=input("enter the name no for update: ")
        address=input("enter the address no for update: ")
        sclass=input("enter the sclass no for update: ")
        sql="update ib18 set name=%s, address=%s, sclass=%s, where rollno=%s  "
        value=[name,address,sclass,rollno]
        self.cursor.execute(sql,value)
        self.mydb.commit()
    def SearchRecord(self):
        rollno=input("enter the roll number ")
        sql="select * from ib18 where rollno=%s"
        value=[rollno]
        self.cursor.execute(sql,value)
        mydata=self.cursor.fetchall()
        cnt=self.cursor.rowcount
        if(cnt>=1):
            print(mydata)
        else:
            print("no record found")
    def deleteRecord(self):
        rollno=input("enter the roll number ")
        sql="delete from ib18 where rollno=%s"
        value=[rollno]
        self.cursor.execute(sql,value)
        self.mydb.commit()
        print("record deleted succssfully")