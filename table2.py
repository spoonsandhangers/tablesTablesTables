"""
This combines file readings from a text file into a table to display information
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("tables tables tables")

frame = Frame(root)
frame.pack(pady=20)

staff = ttk.Treeview(frame, columns=(1,2,3), show='headings', height=8)
staff.pack(side=LEFT)

myheadings = ["name", "staff id", "Salary"]

for count, head in enumerate(myheadings, 1):
	staff.heading(count, text=head)

# opens the text file and reads the contents into a 2D list - data
try:
	myFile = open("staff.txt", "r")
except IOError as e:
	print("The exception", e, "was raised.")
else:
	fileRead = myFile.readlines()
	data = []
	for line in fileRead:
		line = line.rstrip("\n") # removes the \n from the end of the line
		data.append(line.split(","))

# adds each record in the text file (each sublist in data) to the table staff
# note that the values are now referencing the list data
for count, item in enumerate(data,0):
	staff.insert(parent='', index=count, iid=count, values=(item[0], item[1], item[2]))


print(data)

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

root.mainloop()
