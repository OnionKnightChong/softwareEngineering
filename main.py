import MySQLdb
from tkinter import *
from functools import partial

import hashlib

# connect to the database
db = MySQLdb.connect(host="grover.ctuetzgk1e5k.us-east-1.rds.amazonaws.com",    # host address
		user="admin",         # username
		passwd="howard123",  # password
		db="grover")        # database name

# global variables
cur = db.cursor()
currentWindowIndex = 0		# 0: main window 	1: user manage window	2: store manage window


class loginWindow:
	def __init__(self):
		self.tkWindow = Tk()
		self.tkWindow.geometry('400x150')
		self.tkWindow.title('Login')

		self.count = 0		# record how many time password is wrong
		self.loginvalid = False

		#username label and text entry box
		self.usernameLabel = Label(self.tkWindow, text="User Name").grid(row=0, column=0)
		self.username = StringVar()
		self.usernameEntry = Entry(self.tkWindow, textvariable=self.username).grid(row=0, column=1)

		#password label and password entry box
		self.passwordLabel = Label(self.tkWindow,text="Password").grid(row=1, column=0)
		self.password = StringVar()
		self.passwordEntry = Entry(self.tkWindow, textvariable=self.password, show='*').grid(row=1, column=1)

		self.validateLogin = partial(self.validlogin, self.username, self.password)
	
		#login button
		self.loginButton = Button(self.tkWindow, text="Login", command=self.validateLogin).grid(row=4, column=0)

	def validlogin(self, username, password):

		# read from a local file, this file stores legal usernames and their hashed passwords
		# this fild may not be synchronized with database, it needs to be manually synchronized
		u,p = self.username.get(), self.password.get()
		s = p.encode('utf-8')
		ep = hashlib.sha1(s).digest()	# hashed to a 20-byte string
		#print(u, ep)
	
		# search user.conf to find corresponding user and password
		f = open("users.conf")
		
		Lines = f.readlines()
		for l in Lines:
			c = l.split()
			print(c)
			#print(c[1])
			if c[0] == u:
				print("Find user: "+c[0])
				if c[1] == ep:
					self.loginvalid = True
					print("password matched!")
				else:
					print(ep)
					print(len(ep))
					print(c[1])
					print(len(c[1]))
					print("password unmatched!")
					self.count += 1
				break
		f.close()
	
		if self.loginvalid == False:
			#self.passwordEntry.delete(0, 'end')
			if self.usernameEntry is None:
				print("can not change the content")

		if self.loginvalid == True or self.count >= 3:
			tkWindow.destroy()
	
	def showlogin(self):
		self.tkWindow.mainloop()

if __name__ == "__main__":
	l = loginWindow()
	l.showlogin()

	if l.loginvalid == True:
		# this branch mean login success
		# show the main window
		print("Login success!")
	else:
		print("Login failed!")
