"""
Creating tables in Tkinter.

There is no table widget but we can use a function from ttk
called treeview.

You must import ttk from tkinter
Then add a Frame to the root window.
Create a Treeview object with the correct number of columns (see other attributes)
Create a list of headings for the columns
iterate through the heading list adding them to the Treeview object
use the insert function to insert more rows when necessary.
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("tables tables tables")

frame = Frame(root)
frame.pack(pady=20)

# sets up the table with the number of columns required
staff = ttk.Treeview(frame, columns=(1,2,3), show='headings', height=8)
staff.pack(side=LEFT)

# list of column headings for the table
myheadings = ["name", "staff id", "Salary"]

# a new type of for loop.
# this uses the enumerate function to produce a count as
# well as iterating through the myheadings list
# count starts at 1 and increments on each loop
# head is set to each value in turn in the myheadings list.
for count, head in enumerate(myheadings, 1):
	staff.heading(count, text=head) # this line adds the item in myheading to the next column in the staff table

# this inserts the values shown into a row of the staff table
staff.insert(parent='', index=0, iid=0, values=("sarah", "sj2256", 2000))

# settings for the table
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

root.mainloop()
