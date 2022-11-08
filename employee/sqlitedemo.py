import sqlite3
from employee import Employee
conn = sqlite3.connect('employee.db')
cur = conn.cursor()

# cur.execute("""CREATE TABLE employees(
# firstName text,
# lastName text,
# pay integer
# )""")
#
emp1 = Employee('Prah', 'Agnes', 4000)
emp2 = Employee('Zumah', 'Fidles', 8000)

# print(emp1.firstName)
# cur.execute("INSERT INTO employees VALUES (?, ?, ?)",
# (emp1.firstName, emp1.lastName, emp1.pay))
#
# cur.execute("INSERT INTO employees VALUES (:firstName,:lastName,:pay)",
# {'firstName': emp2.firstName, 'lastName': emp2.lastName, 'pay': emp2.pay})
#
cur.execute("SELECT * FROM employees")
print(cur.fetchall())
conn.commit()

conn.close()
