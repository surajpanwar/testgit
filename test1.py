import mysql.connector as abc

mydb = abc.connect(host = "localhost" , user ="root", passwd ="Papa@9969" )

print(mydb)

cursor = mydb.cursor()
#cursor.execute("create database if not exists suraj")
#cursor.execute("use suraj")
#s= cursor.execute("create table if not exists suraj.surajdetails(employee_id int(10), age int, name varchar(30), emp_salary int(10) )")
#q1=cursor.execute(s)



#cursor.execute("show databases")
#print(cursor.fetchall())
