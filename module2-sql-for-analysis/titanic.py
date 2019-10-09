import pandas as pd
import sqlite3
import psycopg2

# Logging
dbname = 'gilolekm'
user = 'gilolekm'
password = ''
host = 'salt.db.elephantsql.com'

# connecting server
pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
pg_curs = pg_conn.cursor()

 # creates db titanic.sqlite3
sl_conn = sqlite3.connect("titanic.sqlite3")
sl_curs = sl_conn.cursor()

 #importing titanic
delete_table = 'DROP TABLE IF EXISTS Titanic'
sl_curs.execute(delete_table)
titanic_data = pd.read_csv('titanic.csv')
titanic_data.Name = titanic_data.Name.replace("'", '', regex=True)
titanic_data.to_sql('Titanic', sl_conn, index_label='id')


 # Create titnic table
create_titanic_table = """
 CREATE TABLE titanic_table (
 survived INT,
 pclass INT,
 name VARCHAR (110),
 sex  VARCHAR(10),
 age FLOAT,
 siblingsSpouses INT,
 parentsChildren INT,
 fare FLOAT
 );
 """

pg_curs.execute(create_titanic_table)

titanic_list= sl_curs.execute("SELECT * FROM Titanic").fetchall()

for n in titanic_list:
    insertinfo = """
        INSERT INTO titanic_table
        (survived, pclass, name, sex, age, siblingsSpouses,
        parentsChildren, fare)
        VALUES """ + str(n[1:]) + ';'
    pg_curs.execute(insertinfo)

# pg_curs.fetchall()
pg_curs.close()
pg_conn.commit()
