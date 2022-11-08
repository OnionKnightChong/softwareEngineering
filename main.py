import MySQLdb
from tkinter import *
from functools import partial

db = MySQLdb.connect(host="grover.ctuetzgk1e5k.us-east-1.rds.amazonaws.com",    # host address
		user="admin",         # username
		passwd="howard123",  # password
		db="grover")        # database name

cur = db.cursor()
loginvalide = False

def validlogin(username, password):
	print(username, password)

def showlogin():
	tkWindow = Tk()
	tkWindow.geometry('400x150')
	tkWindow.title('Login')

	#username label and text entry box
	usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
	username = StringVar()
	usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

	#password label and password entry box
	passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
	password = StringVar()
	passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

	validateLogin = partial(validlogin, username, password)

	#login button
	loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

	tkWindow.mainloop()

if __name__ == "__main__":
	showlogin()

	if loginvalid == True:
		# this branch mean login success
		pass
