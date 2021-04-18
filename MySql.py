import mysql.connector

myDB=mysql.connector.connect(host="localhost",user="Ayush",password="pinknblues", database='practice_database')


# Create a database

myCursor=myDB.cursor()
myCursor.execute("CREATE DATABASE practice_database")

# Create Table in database
myCursor.execute("CREATE TABLE student(Name VARCHAR(100),Father_Name VARCHAR(100),Your_Age INT)")

# Insert Values in Table student:

table_value="""
            INSERT INTO student(Name,Father_Name,Your_Age)VALUES('Suhani Dubey','Rajesh Dubey','14')
            """
try:
    myCursor.execute(table_value)
    myDB.commit()
except Exception:
    myDB.rollback()
print("Data inserted")

# Fetch Data from student

query="""
        SELECT * FROM student
    """
myCursor.execute(query)

records=myCursor.fetchall()

for row in records:
    print("Student Name",row[0])
    print("Father Name",row[1])
    print("Student Age",row[2])

myDB.close()
