import mysql.connector as abc

mydb = abc.connect(host = "localhost" , user ="root", passwd ="Papa@9969" )

cursor = mydb.cursor()
cursor.execute("select employee_id,emp_salary from suraj.surajdetails")

l=[]
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l))
print(type(l[0]))
print(type(l[0][1]))