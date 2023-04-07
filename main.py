
import tkinter as tk
from proj import *
# Course options
COURSE_OPTIONS = {
    "DSA": 1,
    "Modernity": 2,
    "Calc": 3,
    "DM": 4,
    "Bio": 5
}

def mainn(selected_courses):
    return f"You selected courses {', '.join(map(str, selected_courses))}."


def submit():
    selected_courses = [course for course, var in checkboxes.items() if var.get() == 1]
    selected_courses = [COURSE_OPTIONS[course] for course in selected_courses]
    result = mainn(selected_courses)
    output.config(text=result)
root = tk.Tk()
root.title("Course Form")
checkboxes = {}
for course in COURSE_OPTIONS:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=course, variable=var)
    checkbox.pack()
    checkboxes[course] = var
submit = tk.Button(root, text="Submit", command=submit)
submit.pack()
output = tk.Label(root, text="")
output.pack()
root.mainloop()
