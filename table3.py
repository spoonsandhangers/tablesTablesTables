"""
advanced
select a row of the table and perform an operation at the click of a button
in this case it is a salary increase.
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

# this function executes when the button is pressed
def update_item():
	selected = staff.focus() # holds the number of the selected row
	try:
		temp = staff.item(selected, 'values') # values from the row are stored as a tuple
		increase = float(temp[2]) + float(temp[2]) * 0.25 # takes the selected values from the tuple
		staff.item(selected, values=(temp[0], temp[1], increase)) # provides new values to the record
	except IndexError:
		print("no row selected") # prints an error if no row has been selected

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

for count, item in enumerate(data,0):
	staff.insert(parent='', index=count, iid=count, values=(item[0], item[1], item[2]))


print(data)

# creates a button for the update_item function
Button(root, text="Increment Salary", command=update_item).pack()

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

root.mainloop()
