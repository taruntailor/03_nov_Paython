import mysql.connector

con = mysql.connector.connect(
     host="localhost",
    port=3306,
    user="root",
    password="12345678",
    database="paythan_03"
)

# print("connected")
cursor = con.cursor()

# cursor.execute("create database paythan_03")

# qry = "create table emp(id int primary key auto_increment,name varchar(20),email varchar(50))"
# cursor.execute(qry)


# qry = "insert into emp values(0,'DEV','dev@gmail.com')"
# cursor.execute(qry)

qry = "insert into emp(name,email) values(%s,%s)"
val = ('Parth','parth@gmail.com')

cursor.execute(qry,val)

# qry = "update user set email='abc@yahoo.com' where id=2"

# qry = "update user set email=%s where id=%s"
# val = ("xyz@gmail.com",3)
# cursor.execute(qry,val)


# qry = "delete from user where id=1"

# qry = "delete from user where id=%s"
# val = (2,)
# cursor.execute(qry,val)
# con.commit()


# cursor.execute("select * from user")
# data = cursor.fetchmany(3)

# sr = 1
# for i in data:
#     print(sr,end=" ")
#     for k in i:
#         print(k,end=" ")
#     print("")
#     sr+=1