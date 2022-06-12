from tkinter import *

root = Tk()
root.title("Friend Bot")

name = input("What is your name? ")
color = "blue"

def main():
	buttons()
	labels()
	place()

def buttons():
	global button1, button2, button3, button4, button5
	button1 = Button(root, text="Hi!", command=lambda: new("hi"), fg=color)
	button2 = Button(root, text="Great!", command=lambda: new("great"), fg=color)
	button3 = Button(root, text=name, command=lambda: new("name"), fg=color)
	button4 = Button(root, text="Yes!", command=lambda: new("you"), fg=color)
	button5 = Button(root, text="You too!", command=lambda: new("friend"), fg=color)

def labels():
	global label1, label2, label3, label4, label5, label6
	label1 = Label(root, text="Hi!")
	label2 = Label(root, text="How are you?")
	label3 = Label(root, text="What's your name?")
	label4 = Label(root, text="Nice to meet you " + name)
	label5 = Label(root, text="Do you want to be friends?")
	label6 = Label(root, text="Bye!")

def place():
	label1.pack()
	button1.pack()

def new(word):
	if word == "hi":
		label2.pack()
		button2.pack()
	if word == "great":
		label3.pack()
		button3.pack()
	if word == "name":
		label4.pack()
		button4.pack()
	if word == "friend":
		label5.pack()
		button5.pack()
	if word == "you":
		label6.pack()

main()


root.mainloop()
