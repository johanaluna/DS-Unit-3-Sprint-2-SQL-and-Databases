import sqlite3 as sql


conn = sql.connect("northwind_small.sqlite3")
curs = conn.cursor()

q1= """
    SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
    """
print('What are the ten most expensive items (per unit price) in the database?')
print('Answer1:',curs.execute(q1).fetchall())

q2= """
    SELECT AVG(HireDate -BirthDate) FROM Employee;
    """
print('What is the average age of an employee at the time of their hiring?')
print('Answer2:',curs.execute(q2).fetchall())

q3= """
    SELECT City, AVG(HireDate -BirthDate) AS AVGAgeHired
    FROM Employee
    GROUP BY City
    ORDER BY AVGAgeHired DESC;
    """
print('How does the average age of employee at hire vary by city')
print('Answer3:',curs.execute(q3).fetchall())
