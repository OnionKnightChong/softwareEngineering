import MySQLdb
import tkinter

# an update for the code, just for experiment

db = MySQLdb.connect(host="grover.ctuetzgk1e5k.us-east-1.rds.amazonaws.com",    # host address
		user="admin",         # username
		passwd="howard123",  # password
		db="grover")        # database name

cur = db.cursor()

print("-------------query users---------------")
cur.execute("SELECT * FROM USER")
for row in cur.fetchall():
	print(row)

print("-------------query categories---------------")
cur.execute("SELECT * FROM CATEGORY") 
for row in cur.fetchall():
	print(row)

db.close()
