import pandas as pd
from tkinter import *
from datetime import datetime
import tkinter
from tkinter import ttk
from tkinter import messagebox

df = pd.read_csv('Courses.csv')

def Graph_building(df):
    graph = {}
    for index, row in df.iterrows(): # The code will basically iterate over the rows in the csv file 
        course_code = row['Course Name']
        section = row['Course No']
        timings = row[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']].tolist()
        if course_code not in graph:
            graph[course_code] = {'sections': {}}
        graph[course_code]['sections'][section] = {'timings': timings} #the nodes of the graph will contain a nested dictionary which further contains a ditionary for timings of the section
    return graph


def generate_timetables(graph, courses, current_timetable, all_timetables): # This code uses recursion

    if len(current_timetable) == len(courses): #current time table is the temporary dictionary in which it stores the one of the timetables
        all_timetables.append(current_timetable)
        return # will return when the number of courses in temporary dictionary are equal to the courses

    current_course = courses[len(current_timetable)]

    for section in graph[current_course]['sections']:
        new_timetable = current_timetable.copy()
        new_timetable[current_course] = section

        if is_valid_timetable(new_timetable, graph): 
            generate_timetables(graph, courses, new_timetable, all_timetables)


def is_valid_timetable(timetable, graph): # this code is the helper function and is used to find if the combination of the sections are not clashing 
    for day in range(5):
        for course, section in timetable.items():
            timings = graph[course]['sections'][section]['timings']
            start_time, end_time = [datetime.strptime(t, '%H:%M') for t in timings[day].split('-')] # this takes out the specific time of the class of a day 

            for other_course, other_section in timetable.items():
                if other_course != course:
                    other_timings = graph[other_course]['sections'][other_section]['timings']
                    other_start_time, other_end_time = [datetime.strptime(t, '%H:%M') for t in other_timings[day].split('-')]

                    if start_time < other_end_time and end_time > other_start_time: #This compares the timings with other courses
                        return False

    return True


def optimized_timetable(all_timetables, graph): # This function basically check for gaps between classes and the lowest amounts of gaps in a timetable will be returned
    optimized_timetable = None
    min_gaps = float('inf')
    
    for timetable in all_timetables:
        gaps = 0
        for day in range(5):
            day_classes = []
            for c in timetable:
                if graph[c]['sections'][timetable[c]]['timings'][day] != '0-0':
                    day_classes.append(c)
            day_classes.sort(key=lambda c: datetime.strptime(graph[c]['sections'][timetable[c]]['timings'][day].split('-')[0], '%H:%M')) #This is used to format the time for comparison
            for i in range(1, len(day_classes)):
                start_time = datetime.strptime(graph[day_classes[i]]['sections'][timetable[day_classes[i]]]['timings'][day].split('-')[0], '%H:%M')
                end_time = datetime.strptime(graph[day_classes[i-1]]['sections'][timetable[day_classes[i-1]]]['timings'][day].split('-')[1], '%H:%M')
                gaps += (start_time - end_time).total_seconds() / 60
            
        if gaps < min_gaps:
            min_gaps = gaps
            optimized_timetable = timetable
    
    return optimized_timetable

def main(courses_req,option): # This is the function that we have to turn into a form or any app
    courses=[]
    course_preference=[]
    for course in courses_req:
        if courses_req[course]==False:
            continue
        elif courses_req[course]!=None:
            course_preference.append((course,courses_req[course]))
        courses.append(course)
    graph=Graph_building(df)
    current_timetable = {}
    all_timetables = []
    generate_timetables(graph, courses, current_timetable, all_timetables)
    if int(option)==1 :
        filtered_timetable=(optimized_timetable(all_timetables,graph))
        # print(filtered_timetable)
        timeTable([filtered_timetable])
    else:
        new_timetables = []
        for timetable in all_timetables:
            all_preferences_satisfied = True
            for preference in course_preference:
                course_name = preference[0]
                course_no = df.loc[df['Instructor'] == preference[1], "Course No"].values[0]
                if timetable[course_name] == int(course_no):
                    continue
                else:
                    all_preferences_satisfied = False
                    break
            
            if all_preferences_satisfied:
                new_timetables.append(timetable)

        if len(new_timetables) == 0:
            # print()
            tkinter.messagebox.showwarning(title="Error", message="No timetables found that include all preferences")
        else:
            timeTable(new_timetables)
##FRONT END##
courses={}
option=""
def Gen_timetable():
    global courses, option
    Optimized = accept_var.get()
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    ID=ID_entry.get()
    DSA=DSA_combobox.get()
    Modernity=Mordernity_combobox.get()
    DM=DM_combobox.get()
    Calculus=Calculus_combobox.get()
    BioScience=BioScience_combobox.get()

    if not(firstname and lastname and ID):
        error_box = messagebox.showwarning(title="Error", message="First name, last name, and Student ID are required.")
        window.wait_window(error_box)
    elif not DSA:
        error_box = messagebox.showwarning(title="Error", message="Select your DSA Instructor. Select 'Not to be enrolled' if you don't want to be enrolled in this course")
        window.wait_window(error_box)
    elif not DM:
        error_box = messagebox.showwarning(title="Error", message="Select your DM Instructor. Select 'Not to be enrolled' if you don't want to be enrolled in this course")
        window.wait_window(error_box)
    elif not Calculus:
        error_box = messagebox.showwarning(title="Error", message="Select your Calculus Instructor. Select 'Not to be enrolled' if you don't want to be enrolled in this course")
        window.wait_window(error_box)
    elif not Modernity:
        error_box = messagebox.showwarning(title="Error", message="Select your Modernity Instructor. Select 'Not to be enrolled' if you don't want to be enrolled in this course")
        window.wait_window(error_box)
    elif not BioScience:
        error_box = messagebox.showwarning(title="Error", message="Select your BioScience Instructor. Select 'Not to be enrolled' if you don't want to be enrolled in this course")
        window.wait_window(error_box)

    Courses_Required={'DSA':DSA,'DM':DM,'Calc':Calculus,'Modernity':Modernity,'Bio':BioScience}
    for course in Courses_Required:
        if Courses_Required[course]=='Not to be enrolled':
            Courses_Required[course]=False
        if Courses_Required[course]=='Any Instructor':
            Courses_Required[course]=None
    window.destroy()
    courses=Courses_Required
    option=Optimized    
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

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

DSA_label = tkinter.Label(courses_frame, text="DSA")
DSA_combobox = ttk.Combobox(courses_frame, values=['Not to be enrolled','M.Salman','F.Saleem','Any Instructor'])
DSA_label.grid(row=0, column=0)
DSA_combobox.grid(row=0, column=1)

DM_label = tkinter.Label(courses_frame, text="DM")
DM_combobox = ttk.Combobox(courses_frame, values=['Not to be enrolled','R.Ragib','A.Zafar','Any Instructor'])
DM_label.grid(row=1, column=0)
DM_combobox.grid(row=1, column=1)

Calculus_label = tkinter.Label(courses_frame, text="Calculus II")
Calculus_combobox = ttk.Combobox(courses_frame, values=['Not to be enrolled','S.Rana','Y.Kerai','Any Instructor'])
Calculus_label.grid(row=2, column=0)
Calculus_combobox.grid(row=2, column=1)

Mordernity_label = tkinter.Label(courses_frame, text="Mordernity")
Mordernity_combobox = ttk.Combobox(courses_frame, values=['Not to be enrolled','M.Patel','H.Habib','Any Instructor'])
Mordernity_label.grid(row=3, column=0)
Mordernity_combobox.grid(row=3, column=1)

BioScience_label = tkinter.Label(courses_frame, text="BioScience")
BioScience_combobox = ttk.Combobox(courses_frame, values=['Not to be enrolled','A.Nasir','J.Samad','Any Instructor'])
BioScience_label.grid(row=4, column=0)
BioScience_combobox.grid(row=4, column=1)


for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tkinter.LabelFrame(frame,)
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value=False)
terms_check = tkinter.Checkbutton(terms_frame, text= "I want the TimeTable to be optimized",variable=accept_var, onvalue=True, offvalue=False)
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Generate Timetable", command= Gen_timetable)
button.grid(row=3, column=0, padx=20, pady=10)
 
window.mainloop()
##DISPLAY##
def timeTable(all_timetables):
    if all_timetables==[{}]: tkinter.messagebox.showwarning(title="Error", message="No timetables found that include all preferences")
    root = Tk()
    root.title("Timetables")


    style = ttk.Style()
    style.configure("Treeview", background="#2D5F6E", foreground="#f0f0f0", fieldbackground="#3E88A5")
    style.configure("Treeview.Heading", font=("Helvetica", 12), background="#1e404a", foreground="#5F97AA")
  
    # Create a list of tables for each timetable
    tables = []
    for timetable in all_timetables:
        table = ttk.Treeview(root, style='Treeview')
        table["columns"] = ("Course", "Section", "Instructor", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
        table.heading("Course", text="Course")
        table.heading("Section", text="Section")
        table.heading("Instructor", text="Instructor")
        table.heading("Monday", text="Monday")
        table.heading("Tuesday", text="Tuesday")
        table.heading("Wednesday", text="Wednesday")
        table.heading("Thursday", text="Thursday")
        table.heading("Friday", text="Friday")
        table.column("#0", width=0, stretch=NO)
        table.column("Course", width=100, anchor=CENTER)
        table.column("Section", width=100, anchor=CENTER)
        table.column("Instructor", width=150, anchor=CENTER)
        table.column("Monday", width=100, anchor=CENTER)
        table.column("Tuesday", width=100, anchor=CENTER)
        table.column("Wednesday", width=100, anchor=CENTER)
        table.column("Thursday", width=100, anchor=CENTER)
        table.column("Friday", width=100, anchor=CENTER)
        for course, section in timetable.items():
            course_name, course_no = course, int(section)
            k = df.index.get_loc(df[df["Course No"] == course_no].index[0])
            row = df.iloc[k]
            course_instructor,mon,tues,wed,thurs,fri=row["Instructor"],row["Monday"],row["Tuesday"],row["Wednesday"],row["Thursday"],row["Friday"]
            table.insert("", "end", text="", values=(course_name, course_no, course_instructor, mon, tues, wed, thurs, fri))
        tables.append(table)

    current_table = 0
    tables[current_table].grid(row=0, column=1, sticky="nsew")

    def next_table():
        nonlocal current_table
        tables[current_table].grid_forget()
        current_table += 1
        if current_table == len(tables):
            root.destroy()
        else:
            tables[current_table].grid(row=0, column=1, sticky="nsew")
        current_table_label.config(text=f"Timetable number {current_table + 1} of {len(tables)}")

    def prev_table():
        nonlocal current_table
        tables[current_table].grid_forget()
        current_table -= 1
        if current_table < 0:
            current_table = 0
        tables[current_table].grid(row=0, column=1, sticky="nsew")
        current_table_label.config(text=f"Timetable number {current_table + 1} of {len(tables)}")

    
    prev_button = ttk.Button(root, text="<Prev", command=prev_table)
    prev_button.grid(row=1, column=0, pady=10, padx=10)

    current_table_label = ttk.Label(root, text=f"Timetable number {current_table + 1} of {len(tables)}")
    current_table_label.grid(row=1, column=1, pady=10)

    next_button = ttk.Button(root, text="Next>", command=next_table)
    next_button.grid(row=1, column=2, pady=10, padx=10)
    
    root.mainloop()


main(courses,option)
