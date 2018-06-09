import sqlite3
conn=sqlite3.connect('employee.db')
cursor=conn.execute("SELECT id,name,address,salary from EMPLOYEE")
for row in cursor:
    print("id=",row[0])
    print("name=",row[1])
    print("address=",row[2])
    print("salary",row[3])
print("operaton done successfully")
conn.close()