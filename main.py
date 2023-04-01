import pandas as pd
from collections import deque

df = pd.read_csv("/Users/aliimran/Desktop/DSA Project/Courses.csv")
data = df.values.tolist()

def Time_table_generator(data):
    G = {}

    for course in data:
        course_name = course[df.columns.get_loc("Course Name")]
        course_no = course[df.columns.get_loc("Course No")]
        node = f"{course_name} {course_no}"
        G[node] = []
        neighbors = []
        for other_course in data:
            if course_name == other_course[df.columns.get_loc("Course Name")]:
                continue

            clash = False
            gaps = 0
            for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                course_time = course[df.columns.get_loc(day)]
                other_course_time = other_course[df.columns.get_loc(day)]
                if course_time != "0-0" and other_course_time != "0-0":
                    course_start, course_end = [float(t) for t in course_time.split("-")]
                    other_course_start, other_course_end = [float(t) for t in other_course_time.split("-")]
                    if course_start <= other_course_end and course_end >= other_course_start:
                        clash = True
                        break
                    if course_end < other_course_start:
                        gaps += round(abs(other_course_start - course_end ))
                    elif other_course_end < course_start:
                        gaps += round(abs(course_start - other_course_end ))

            if not clash:
                other_course_name = other_course[df.columns.get_loc("Course Name")]
                other_course_no = other_course[df.columns.get_loc("Course No")]
                neighbor = f"{other_course_name} {other_course_no}"
                neighbors.append((neighbor, gaps))
        G[node] = neighbors

    return G

def possible_timetables(G, courses):
    Flag=False
    for idx,course in enumerate(courses):
            otherCourses=courses[idx+1:]+courses[:idx] 
            current_course=[course[0] for course in G[course]]
            for ele in otherCourses:
                if ele in current_course:
                    Flag=True
                else:
                    Flag=False
                    break
    if Flag:
        timeTable(data,courses)
    else:
        print("Try other combinations")
    
def timeTable(data,courses):
    for course in courses:
        course_name,course_no=course.split()
        k = df.index.get_loc(df[df["Course No"] == int(course_no)].index[0])
        row = df.iloc[k]
        course_instructor,mon,tues,wed,thurs,fri=row["Instructor"],row["Monday"],row["Tuesday"],row["Wednesday"],row["Thursday"],row["Friday"]
        mon_str = f"Monday {mon}" if mon != "0-0" else ""
        tues_str = f"Tuesday {tues}" if tues != "0-0" else ""
        wed_str = f"Wednesday {wed}" if wed != "0-0" else ""
        thurs_str = f"Thursday {thurs}" if thurs != "0-0" else ""
        fri_str = f"Friday {fri}" if fri != "0-0" else ""

        print(f"{course_name} - {course_no} - {course_instructor} : Timings => {mon_str} - {tues_str} - {wed_str} - {thurs_str} - {fri_str}")




G=Time_table_generator(data)
course_names = ["Modernity 20", "Bio 50", "DSA 10"]












