import MySQLdb
from tkinter import *
from functools import partial

def downloadallusers(filename='users.conf'):
	print("Downloading all users begins"+"-"*20)
	
	# connect to database
	print("---connect to database")
	db = MySQLdb.connect(host="grover.ctuetzgk1e5k.us-east-1.rds.amazonaws.com", user="admin", passwd="howard123",  db="grover")

	# open the file
	print("---open storing file");
	f = open(filename, 'w')
	
	cur = db.cursor()
	cur.execute("SELECT * FROM USER where admin=1")
	for row in cur.fetchall():
		print(row[0], row[2]);
		f.write(row[0])
		f.write(" ")
		f.write(row[2])
		f.write("\n")
	print("---close storing file");
	f.close()
	print("---disconnect to database")
	db.close()
	print("Downloading all users ends!"+"-"*20);

if __name__ == '__main__':
	downloadallusers()
