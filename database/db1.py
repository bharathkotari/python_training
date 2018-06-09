import sqlite3
conn=sqlite3.connect('employee.db')
try:
	conn.execute('CREATE TABLE employee(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,ADDRESS CHAR(50),SALARY REAL)')
	print("table created successfully")
except:pass

conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1,'RAM',28,'BANGLORE',25000)")
conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,'GOPAL',25,'BANGLORE',30000)")
conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY) VALUES(3,'MOHAN',30,'BANGLORE',60000)")
conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY) VALUES(4,'KUMAR',28,'BANGLORE',10000)")
conn.commit()
print("records created successfully")
conn.close()

conn=sqlite3.connect('employee.db')
cursor=conn.execute("SELECT id,name,address,salary from EMPLOYEE")
for row in cursor:
    print("id=",row[0])
    print("name=",row[1])
    print("address=",row[2])
    print("salary",row[3])
print("operaton done successfully")
conn.close()