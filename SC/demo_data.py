import sqlite3 as sql

conn = sql.connect("demo_data.sqlite3")
curs = conn.cursor()

delete_table = 'DROP TABLE IF EXISTS demo'
curs.execute(delete_table)

q1 = """ CREATE TABLE demo (
    s TEXT,
    x INT,
    y INT);
    """
curs.execute(q1).fetchall()

q2 = """ INSERT INTO demo (s, x, y)
    VALUES ('g', 3, 9),
           ('v', 5, 7),
           ('f', 8, 7)
     """
curs.execute(q2).fetchall()
conn.commit()

count_r = """
        SELECT COUNT(*) FROM demo;
        """
print('Number of rows=', curs.execute(count_r).fetchall()[0][0])

rows_5 = """
        SELECT COUNT(*)
        FROM demo
        WHERE x >= 5 AND y >= 5;
        """
print('Number of rows with at least 5=', curs.execute(rows_5).fetchall()[0][0])

unique_values = """
                SELECT COUNT(DISTINCT y) FROM demo;
                """
print('Unique Values in Y column=', curs.execute(unique_values).fetchall()[0][0])

curs.close()
conn.commit()
