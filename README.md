# DSA-Proj-Main
README
This Python code helps in generating optimized timetables for a given set of courses by taking into account the timings and sections of each course, and checking for clashes between the timings of the sections. The program uses the pandas library to read a CSV file that contains information about the courses, including their name, course number, instructor, and timings for each day of the week. The Tkinter library is used to display the generated timetables in a user-friendly format.

The program uses a graph-based approach to generate the timetables. The course sections are represented as nodes in the graph, and the timings for each section are stored as a nested dictionary. The program then uses a recursive function to generate all possible combinations of sections for the given set of courses. For each combination, the program checks if the timings for the sections do not clash with each other. If a valid combination is found, it is added to a list of all possible timetables.

The function Graph_building is used to create the graph for the given set of courses. The function takes the course information in the form of a pandas dataframe and returns a nested dictionary that contains the sections and timings for each course.

The function generate_timetables is the main function that generates all possible timetables for the given set of courses. It takes the graph, a list of courses, a current timetable, and a list of all timetables generated so far as input. It uses recursion to generate all possible combinations of course sections and checks for clashes between timings.

The function is_valid_timetable is a helper function that checks if a given timetable is valid or not. It checks for clashes between the timings of the sections of different courses.

The function timeTable is used to display the generated timetables in a user-friendly format using the Tkinter library. It creates a Treeview widget for each generated timetable and populates it with the relevant information from the CSV file.

The function optimized_timetable is used to generate optimized timetables by checking for gaps between classes and selecting the timetable with the lowest amount of gaps.

To use the program, you need to provide a CSV file containing information about the courses in a specific format. The CSV file should contain columns for Course Name, Course No, Instructor, Monday, Tuesday, Wednesday, Thursday, and Friday, where each column represents the timings for the respective day of the week. The timings should be in the format HH:MM-HH:MM.

Once you have the CSV file, you can run the program and enter the names of the courses for which you want to generate timetables. The program will generate all possible timetables and display them in a user-friendly format using the Tkinter library.
