#create section class

class Section:
    def init(self, id, course_symbol, course_id, section, is_theory, course_title, start_time, end_time, days_type):
        self.id = id
        self.course_symbol = course_symbol
        self.course_id = course_id
        self.section = section
        self.is_theory = is_theory
        self.course_title = course_title
        self.start_time = start_time
        self.end_time = end_time
        self.days_type = days_type


# import csv file
import pandas as pd

df = pd.read_excel("mujadwill.xlsx")

sections = []
# create a days_type directory which takes key number and returns the days as t, m, w, r, f

for index, row in df.iterrows():
    section = Section()
    days = []
    # days columns are from column 17 to 21
    # if the column has any value, add it to the days list
    for i in range(17, 22):
        if row[i] == row[i]:
            days.append(row[i])
    section.init(index,row['المقرر'], row['رقمه'], row['الشعبة'], row['رمز الجدولة'], row['عنوان المقرر'], row['البداية'], row['النهاية'], days)

    sections.append(section)


# loop through the sections list and print the course_title
for section in sections:

    print(section.days_type)

