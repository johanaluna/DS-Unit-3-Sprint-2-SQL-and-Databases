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


#output
"""
What are the ten most expensive items (per unit price) in the database?
('Answer1:', [
(u'C\xf4te de Blaye', 263.5),
(u'Th\xfcringer Rostbratwurst', 123.79),
(u'Mishi Kobe Niku', 97),
(u"Sir Rodney's Marmalade", 81),
(u'Carnarvon Tigers', 62.5),
(u'Raclette Courdavault', 55),
(u'Manjimup Dried Apples', 53),
(u'Tarte au sucre', 49.3),
(u'Ipoh Coffee', 46),
(u'R\xf6ssle Sauerkraut', 45.6)])
"""


q2= """
    SELECT AVG(HireDate -BirthDate) FROM Employee;
    """
print('What is the average age of an employee at the time of their hiring?')
print('Answer2:',curs.execute(q2).fetchall())

#output
"""
What is the average age of an employee at the time of their hiring?

('Answer2:', [(37.22222222222222,)])
"""


q3= """
    SELECT City, AVG(HireDate -BirthDate) AS AVGAgeHired
    FROM Employee
    GROUP BY City
    ORDER BY AVGAgeHired DESC;
    """
print('How does the average age of employee at hire vary by city')
print('Answer3:',curs.execute(q3).fetchall())

#output
"""
How does the average age of employee at hire vary by city
('Answer3:', [
(u'Redmond', 56.0),
(u'Seattle', 40.0),
(u'Tacoma', 40.0),
(u'London', 32.5),
(u'Kirkland', 29.0)])
"""


q4 ="""
    SELECT ProductName, CompanyName, UnitPrice
    FROM Product
    INNER JOIN Supplier ON SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC LIMIT 10
    """
print('What are the ten most expensive items (per unit price) in the database and their suppliers?')
print('Answer4:',curs.execute(q4).fetchall())

#output
"""
('Answer4:', [
(u'C\xf4te de Blaye', u'Aux joyeux eccl\xe9siastiques', 263.5),
(u'Th\xfcringer Rostbratwurst', u'Plutzer Lebensmittelgro\xdfm\xe4rkte AG', 123.79),
(u'Mishi Kobe Niku', u'Tokyo Traders', 97),
(u"Sir Rodney's Marmalade", u'Specialty Biscuits, Ltd.', 81),
(u'Carnarvon Tigers', u'Pavlova, Ltd.', 62.5),
(u'Raclette Courdavault', u'Gai p\xe2turage', 55),
(u'Manjimup Dried Apples', u"G'day, Mate", 53),
(u'Tarte au sucre', u"For\xeats d'\xe9rables", 49.3),
(u'Ipoh Coffee', u'Leka Trading', 46),
(u'R\xf6ssle Sauerkraut',u'Plutzer Lebensmittelgro\xdfm\xe4rkte AG', 45.6)])
"""


q5 = """
     SELECT CategoryName
     FROM Category
     INNER JOIN Product
     ON Category.Id = CategoryId
     GROUP BY CategoryId
     ORDER BY COUNT(DISTINCT Product.Id) DESC LIMIT 1;
     """
print('What is the largest category (by number of unique products in id)')
print('Answer5:',curs.execute(q5).fetchall()[0][0])

#output
"""
What is the largest category (by number of unique products in id)
('Answer5:', u'Confections')
"""


q6 = """
     SELECT FirstName, LastName
     FROM Employee
     INNER JOIN EmployeeTerritory
     ON EmployeeTerritory.EmployeeId = EmployeeId
     GROUP BY EmployeeId
     ORDER BY COUNT(DISTINCT TerritoryId) DESC LIMIT 1;
     """
print(' Who\'s the employee with the most territories? Use TerritoryId \
(not name, region, or other fields) as the unique identifier for territories)')
print('Answer6:',curs.execute(q6).fetchall())

#output
"""
Who's the employee with the most territories? Use TerritoryId (not name, region, or othe
r fields) as the unique identifier for territories)
('Answer6:', [(u'Anne', u'Dodsworth')])
"""
