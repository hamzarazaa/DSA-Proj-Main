import pandas as pd
from datetime import datetime, timedelta
df = pd.read_csv('Courses.csv')

def Graph_building(df):
    graph = {}
    for index, row in df.iterrows():
        course_code = row['Course Name']
        section = row['Course No']
        timings = row[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']].tolist()
        if course_code not in graph:
            graph[course_code] = {'sections': {}}
        graph[course_code]['sections'][section] = {'timings': timings}
    return graph


def generate_timetables(graph, courses, current_timetable, all_timetables):
    if len(current_timetable) == len(courses):
        all_timetables.append(current_timetable)
        return

    current_course = courses[len(current_timetable)]

    for section in graph[current_course]['sections']:
        new_timetable = current_timetable.copy()
        new_timetable[current_course] = section

        if is_valid_timetable(new_timetable, graph):
            generate_timetables(graph, courses, new_timetable, all_timetables)


def is_valid_timetable(timetable, graph):
    for day in range(5):
        for course, section in timetable.items():
            timings = graph[course]['sections'][section]['timings']
            start_time, end_time = [datetime.strptime(t, '%H:%M') for t in timings[day].split('-')]

            for other_course, other_section in timetable.items():
                if other_course != course:
                    other_timings = graph[other_course]['sections'][other_section]['timings']
                    other_start_time, other_end_time = [datetime.strptime(t, '%H:%M') for t in other_timings[day].split('-')]

                    if start_time < other_end_time and end_time > other_start_time:
                        return False

    return True

def timeTable(all_timetables):
    for timetable in all_timetables:
        for course in timetable:
            course_name,course_no=course,timetable[course]
            k = df.index.get_loc(df[df["Course No"] == int(course_no)].index[0])
            row = df.iloc[k]
            course_instructor,mon,tues,wed,thurs,fri=row["Instructor"],row["Monday"],row["Tuesday"],row["Wednesday"],row["Thursday"],row["Friday"]
            mon_str = f"Monday {mon}" if mon != "0-0" else ""
            tues_str = f"Tuesday {tues}" if tues != "0-0" else ""
            wed_str = f"Wednesday {wed}" if wed != "0-0" else ""
            thurs_str = f"Thursday {thurs}" if thurs != "0-0" else ""
            fri_str = f"Friday {fri}" if fri != "0-0" else ""

            print(f"{course_name} - {course_no} - {course_instructor} : Timings => {mon_str} - {tues_str} - {wed_str} - {thurs_str} - {fri_str}")
        print("\n"*2)

def main():
    courses_dict={1:"DSA",2:"Modernity",3:"Calc",4:"DM",5:"Bio"}
    num_of_course=int(input("PLEASE ENTER THE NUMBER OF COURSES YOU WANT TO SELECT \n"))
    courses=[]
    course_preference=[]
    print("Please enter your courses one by one")
    for i in range(num_of_course):
        course_name=int(input("DSA => 1 , Modernity => 2 , Calc => 3 , DM => 4 , Bio => 5 \n"))
        courses.append(courses_dict[course_name])
        course_no=input("IF YOU WANT A SPECIFIC SECTION OF ANY COURSES PLEASE ENTER THE SECTION NUMBER: \n")
        if course_no!="": course_preference.append((courses_dict[int(course_name)],int(course_no)))
    graph=Graph_building(df)
    current_timetable = {}
    all_timetables = []
    generate_timetables(graph, courses, current_timetable, all_timetables)
    print(all_timetables)
    if len(course_preference)==0:
        timeTable(all_timetables)
    else:
        new_timetables = []
        for timetable in all_timetables:
            all_preferences_satisfied = True
            for preference in course_preference:
                course_name = preference[0]
                course_no = preference[1]
                if timetable[course_name] == int(course_no):
                    continue
                else:
                    all_preferences_satisfied = False
                    break
            
            if all_preferences_satisfied:
                new_timetables.append(timetable)

        if len(new_timetables) == 0:
            print("No timetables found that include all preferences")
        else:
            timeTable(new_timetables)
main()
