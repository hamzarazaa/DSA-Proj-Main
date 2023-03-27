import pandas as pd
df = pd.read_csv(r"https://raw.githubusercontent.com/hamzarazaa/DSA-Proj-Main/main/Courses.csv")
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
            for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                course_time = course[df.columns.get_loc(day)]
                other_course_time = other_course[df.columns.get_loc(day)]
                if course_time != "0-0" and other_course_time != "0-0":
                    course_start, course_end = [int(t) for t in course_time.split("-")]
                    other_course_start, other_course_end = [int(t) for t in other_course_time.split("-")]
                    if course_start <= other_course_end and course_end >= other_course_start:
                        clash = True
                        break
        
            if not clash:
                other_course_name = other_course[df.columns.get_loc("Course Name")]
                other_course_no = other_course[df.columns.get_loc("Course No")]
                neighbor = f"{other_course_name} {other_course_no}"
                neighbors.append(neighbor)
        G[node] = neighbors

    return G

print(Time_table_generator(data))
