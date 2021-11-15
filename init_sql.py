import sqlite3

conn = sqlite3.connect('./src/db/database.sqlite')
print('Opened database successfully')

conn.execute("CREATE TABLE projects (id	TEXT NOT NULL, title	TEXT NOT NULL, 	slug TEXT NOT NULL UNIQUE, content	TEXT NOT NULL, 	category	TEXT NOT NULL, 	project_url	TEXT NOT NULL UNIQUE,image_url	TEXT NOT NULL UNIQUE, 	PRIMARY KEY(ID) )")


print ('Table created successfully')
conn.close()
