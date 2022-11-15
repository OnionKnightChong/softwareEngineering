import MySQLdb
from tkinter import *
from functools import partial

import hashlib

db = MySQLdb.connect(host="grover.ctuetzgk1e5k.us-east-1.rds.amazonaws.com", user="admin", passwd="howard123",  db="grover")  

cur = db.cursor()
updatelist = []

cur.execute("SELECT * FROM USER where admin=0")
#cur.execute("SELECT * FROM USER where admin=1")
for row in cur.fetchall():
	print(row)

	user_id = row[0]
	password = row[2]
	s = password.encode('utf-8')
	ep = hashlib.sha1(s).digest()
	print(ep)
	updatelist.append([user_id, ep])
	#updatesql = "update  user set password = "+ep+" where user_id = '" + user_id +"';"
	#print(updatesql)
	#self.cursor.execute("INSERT INTO test (password) VALUE (%s)", (hash_pass,))

print("item number:" + str(len(updatelist)))


for t in updatelist:
	user_id, ep = t
	cur.execute("update USER set password = %s where user_id = %s;",(ep, user_id))

cur.execute("commit;")

db.close()
