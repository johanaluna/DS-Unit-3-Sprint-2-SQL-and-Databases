import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

q1 = ' SELECT COUNT (DISTINCT  character_id)\
       FROM charactercreator_character;'

print('How many total Characters are there',
       curs.execute(q1).fetchall()[0][0])

q2 = ' SELECT COUNT (DISTINCT  character_id) \
       FROM charactercreator_character_inventory;'

print('How many of each specific subclass?\n character_inventory',\
curs.execute(q2).fetchall()[0][0])

q3 = ' SELECT COUNT (DISTINCT  character_ptr_id) \
       FROM charactercreator_mage;'


print('How many of each specific subclass?\n charactercreator_mage',\
curs.execute(q3).fetchall()[0][0])

q4 = ' SELECT COUNT (DISTINCT  character_ptr_id)\
       FROM charactercreator_thief;'

print('How many of each specific subclass?\n charactercreator_thief',\
curs.execute(q4).fetchall()[0][0])

q5 = ' SELECT COUNT (DISTINCT  character_ptr_id)\
       FROM charactercreator_cleric;'

print('How many of each specific subclass?\n charactercreator_cleric',\
curs.execute(q5).fetchall()[0][0])

q6 = ' SELECT COUNT (DISTINCT  character_ptr_id)\
       FROM charactercreator_fighter;'

print('How many of each specific subclass?\n charactercreator_fighter',\
curs.execute(q6).fetchall()[0][0])

q7 = ' SELECT COUNT (item_id) \
       FROM charactercreator_character_inventory;'

print('How many total Items?',\
curs.execute(q7).fetchall()[0][0])

q8 = ' SELECT COUNT(cci.character_id) \
       FROM charactercreator_character_inventory AS cci, \
       armory_item AS ai,  armory_weapon AS aw \
       WHERE cci.item_id = ai.item_id AND \
       ai.item_id = aw.item_ptr_id'

print('How many of the Items are weapons?',\
curs.execute(q8).fetchall()[0][0])

q9 = ' SELECT COUNT(cci.item_id)\
       FROM charactercreator_character_inventory as cci\
       WHERE cci.item_id NOT IN (SELECT ai.item_id \
       FROM armory_item AS ai , armory_weapon AS aw\
       WHERE ai.item_id  = aw.item_ptr_id)'

print('How many are not?',\
curs.execute(q9).fetchall()[0][0])

q10 = ' SELECT  COUNT (cci.item_id), cci.character_id\
        FROM charactercreator_character_inventory AS cci\
        GROUP BY cci.character_id LIMIT 20;'

print('How many Items does each character have? (Return first 20 rows)',\
curs.execute(q10).fetchall())

q11 = ' SELECT cci.character_id, SUM (CASE WHEN cci.item_id IN\
        ( SELECT ai.item_id FROM armory_item AS ai, armory_weapon AS aw\
        WHERE ai.item_id = aw.item_ptr_id\
        ) THEN 1 ELSE 0 END)\
        FROM charactercreator_character_inventory AS cci\
        GROUP BY cci.character_id LIMIT 20;'

print('How many Weapons does each character have? (Return first 20 rows)',\
curs.execute(q11).fetchall())

q12 = ' SELECT AVG(count_items)\
        FROM (\
        SELECT COUNT(cci.item_id ) AS count_items\
        FROM charactercreator_character_inventory AS cci\
	    GROUP BY cci.character_id);'

print('On average, how many Items does each Character have?',\
curs.execute(q12).fetchall()[0][0])

q13 = ' SELECT AVG(weapon_count)\
        FROM (SELECT cci.character_id, \
        SUM (CASE WHEN cci.item_id IN (\
        SELECT ai.item_id FROM armory_item AS ai, \
        armory_weapon AS aw \
        WHERE ai.item_id = aw.item_ptr_id)\
        THEN 1 ELSE 0 END) AS weapon_count\
        FROM charactercreator_character_inventory AS cci\
        GROUP BY cci.character_id );'

print('On average, how many Weapons does each character have?',\
curs.execute(q13).fetchall()[0][0])

curs.close()
conn.commit()
