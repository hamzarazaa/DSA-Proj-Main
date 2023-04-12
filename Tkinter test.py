import tkinter
from tkinter import ttk
from tkinter import messagebox


def Gen_timetable():
    accepted = accept_var.get()
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    ID=ID_entry.get()
    DSA=DSA_combobox.get()
    Mordernity=Mordernity_combobox.get()
    DM=DM_combobox.get()
    Calculus=Calculus_combobox.get()
    Bioscience=BioScience_combobox.get()
    if not(firstname and lastname and ID):
        tkinter.messagebox.showwarning(title="Error", message="First name, last name, and Student ID are required.")
    if not DSA:
        tkinter.messagebox.showwarning(title="Error", message="Select your DSA Instructor. Select 'Not to be enrolled' if you don't want to be enrolled in this course")
    if not DM:
        tkinter.messagebox.showwarning(title="Error", message="Select your DM Instructor. Select 'Not to be enrolled' if you don't want to be enrolled in this course")
    if not Calculus:
        tkinter.messagebox.showwarning(title="Error", message="Select your Calculus Instructor. Select 'Not to be enrolled' if you don't want to be enrolled in this course")
    if not Mordernity:
        tkinter.messagebox.showwarning(title="Error", message="Select your Mordernity Instructor. Select 'Not to be enrolled' if you don't want to be enrolled in this course")
    if not Bioscience:
        tkinter.messagebox.showwarning(title="Error", message="Select your Bioscience Instructor. Select 'Not to be enrolled' if you don't want to be enrolled in this course")
###FRONT END
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="Student Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)
Id_label = tkinter.Label(user_info_frame, text="Student ID")
Id_label.grid(row=0, column=2)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
ID_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
ID_entry.grid(row=1, column=2)

# title_label = tkinter.Label(user_info_frame, text="Title")
# title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
# title_label.grid(row=0, column=2)
# title_combobox.grid(row=1, column=2)

# age_label = tkinter.Label(user_info_frame, text="Age")
# age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
# age_label.grid(row=2, column=0)
# age_spinbox.grid(row=3, column=0)

# nationality_label = tkinter.Label(user_info_frame, text="Nationality")
# nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
# nationality_label.grid(row=2, column=1)
# nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

DSA_label = tkinter.Label(courses_frame, text="DSA")
DSA_combobox = ttk.Combobox(courses_frame, values=['Not to be enrolled','Salman, Muhammad','Saleem,Fahad'])
DSA_label.grid(row=0, column=0)
DSA_combobox.grid(row=0, column=1)

DM_label = tkinter.Label(courses_frame, text="DM")
DM_combobox = ttk.Combobox(courses_frame, values=['Not to be enrolled','R.Ragib','A.Zafar'])
DM_label.grid(row=1, column=0)
DM_combobox.grid(row=1, column=1)

Calculus_label = tkinter.Label(courses_frame, text="Calculus II")
Calculus_combobox = ttk.Combobox(courses_frame, values=['Not to be enrolled','S.Rana','Y.Kerai'])
Calculus_label.grid(row=2, column=0)
Calculus_combobox.grid(row=2, column=1)

Mordernity_label = tkinter.Label(courses_frame, text="Mordernity")
Mordernity_combobox = ttk.Combobox(courses_frame, values=['Not to be enrolled','M.Patel','	H.Habib'])
Mordernity_label.grid(row=3, column=0)
Mordernity_combobox.grid(row=3, column=1)

BioScience_label = tkinter.Label(courses_frame, text="BioScience")
BioScience_combobox = ttk.Combobox(courses_frame, values=['Not to be enrolled','A.Nasir','J.Samad'])
BioScience_label.grid(row=4, column=0)
BioScience_combobox.grid(row=4, column=1)


# registered_label = tkinter.Label(courses_frame, text="Registration Status")

# reg_status_var = tkinter.StringVar(value="Not Registered")
# registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
#                                        variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

# registered_label.grid(row=0, column=0)
# registered_check.grid(row=1, column=0)

# numcourses_label = tkinter.Label(courses_frame, text= "# Completed Courses")
# numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
# numcourses_label.grid(row=0, column=1)
# numcourses_spinbox.grid(row=1, column=1)

# numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
# numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
# numsemesters_label.grid(row=0, column=2)
# numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tkinter.LabelFrame(frame,)
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Optimized")
terms_check = tkinter.Checkbutton(terms_frame, text= "I want the TimeTable to be optimized",variable=accept_var, onvalue="Optimized", offvalue="Not Optimized")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Generate Timetable", command= Gen_timetable)
button.grid(row=3, column=0, padx=20, pady=10)
 
window.mainloop()