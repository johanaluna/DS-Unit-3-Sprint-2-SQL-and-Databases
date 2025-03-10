# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ltKIUiOSCx77S9WCaC7yQijfcjg0aZcp
"""

# gettting IP Address for whitelist
# RUN THIS CELL YOURSELF TO GET YOUR IP FOR WHITE LISTTING
!curl ipecho.net/plain

# In Mongo Create a new Cluster
# to choose my own application with my ip address, choose user name = admin and write the password
# to choose python and version 3.4
# to choose  drive and copy the code

# user =  admin
# pass ="TODO"

# Check python version
import sys
print(sys.version)

# import mongo
!pip install pymongo

!pip install --upgrade dnspython

import pymongo

#connecting to mango databases and assigning to the db object
client = pymongo.MongoClient("mongodb://admin:password@cluster0-shard-00-00-jfno6.mongodb.net:27017,cluster0-shard-00-01-jfno6.mongodb.net:27017,cluster0-shard-00-02-jfno6.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

db

db.test

help(db)

dir(db)

client.nodes

# Insert a document
db.test.insert_one({'x': 1})

#Count how many documents
db.test.count_documents({'x': 1})

# find a document that has this condition 'x':1
db.test.find_one({'x':1})

# find all the documents that has this condition 'x':1
db.test.find({'x':1})

# As we can see the last command just gave us a cursor location then
# We have to save everything in cursor and list the content of that cursor
curs= db.test.find({'x':1})

list(curs)

register1  = {
    'fisrt_name' : ['Andres', 'Felipe'],
    'last_name' : 'Lopez',
    'years_old': 30,
    'sex':'m'
}

register2 = {
    'fisrt_name' : 'Johana',
    'last_name' : 'Luna',
    'years_old': 32,
    'sex':'f'
}

register3  = {
    'fisrt_name' : 'Gustavo',
    'last_name' : 'Luna',
    'years_old': 95,
    'sex':'m'
}

db.test.insert_many([register1,register2,register3])

list(db.test.find())

#create more docs with a loop

more_docs = []
for i in range(30):
    doc = {'even': i % 2 == 0}
    doc['value'] = i
    more_docs.append(doc)

more_docs

db.test.insert_many(more_docs)

list(db.test.find({'even':False}))

list(db.test.find({'fisrt_name' : 'Gustavo'}))

# db.collection.updateOne(filter, update, options)
#$inc	Increments the value of the field by the specified amount.

db.test.update_one({'value':9},
                   {'$inc': {'value':3}})

#check the results
list(db.test.find())

db.test.update_many({'even': True},
                   {'$inc': {'value':100}})

list(db.test.find({'even':True}))

#delecte false values
db.test.delete_many({'even':False})

list(db.test.find())

### EXAMPLE OF INSERTION A new object in our yesterday's example

rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)

db.test.insert_one({'rpg_character': rpg_character})

db.test.find_one({'rpg_character': rpg_character})

db.test.insert_one({
    'sql_id': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
})

list(db.test.find())
