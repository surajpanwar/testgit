import mysql.connector as abc

mydb = abc.connect(host = "localhost" , user ="root", passwd ="Papa@9969" )



cursor = mydb.cursor()

s= "insert into suraj.surajdetails values(12,41,'Vibhor',10)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
mydb.commit()
cursor.execute("select * from suraj.surajdetails")
for i in cursor.fetchall():
    print(i)
## "varchar while inserting values usimg python use single quotes"