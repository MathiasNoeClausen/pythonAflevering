import random
import matplotlib.pyplot as plt
class Student():
    def __init__(self, name, datasheet, gender, image_url):
        self.datasheet = datasheet
        self.name = name
        self.gender = gender
        self.image_url = image_url

    def __repr__(self):
       return 'Student(%r, %r, %r, %r)' % (self.datasheet, self.name, self.gender, self.image_url)

    #def get_avg_grade():





class DataSheet():
    def __init__(self, courses):
        self.courses = courses
    
    def __repr__(self):
        return 'DataSheet(%r)' % (self.courses)

   # def get_grades_as_list():




class Course():
    def __init__(self, name, teacher, classroom, ECTS, grade):
        self.name = name
        self.teacher = teacher
        self.classroom = classroom
        self.ECTS = ECTS
        self.grade = grade

    
    def __repr__(self):
        return 'Course(%r, %r, %r, %r)' % (self.name, self.teacher, self.ECTS, self.grade)


def generate_students(number):
    grades = [0,2,4,7,10,12]
    course_list = ['GameDev', 'Python', 'Security']
    names = ['Mathias', 'David','Gustav', 'Rasmus', 'Joachim']
    gender = ['Male', 'Female']
        
    for x in range(0, number):
        with open('/home/jovyan/python_handin_template/week3.csv', 'a') as file_object:
            course = Course(random.choice(course_list), 'Thomas', 'Class E', 10, random.choice(grades))
            data_sheet = DataSheet([course])
            name = random.choice(names)
            student = Student(name, course, random.choice(gender), 'image_url')
                

            write_to_csv = 'Stud_name: {name}, course: {course}, gender: {gender}, teacher: {teacher}, classroom: {classroom}, ECTS: {ECTS}, grade: {grade}, image_url: {image_url}'.format(
                name=student.name, course=course.name, gender=student.gender, teacher=course.teacher, classroom=course.classroom, ECTS=course.ECTS, grade=course.grade, image_url=student.image_url)
            file_object.write(write_to_csv + '\n')
            
#generate_students(1)



def read_csv(input_file):

    with open(input_file, 'r') as file_object:
        for line in file_object:
            row = line.split(',')
            name, course_name, gender, teacher, classroom, ECTS, grade, image_url = [i.strip() for i in row]
            course = Course(course_name, teacher, classroom, ECTS, grade)
            datasheet = DataSheet([course])
            student = Student(name, datasheet, gender, image_url)
            
            #sorted_grades = sorted(grade)
            print(name, image_url, grade)
          
input_file = ('/home/jovyan/python_handin_template/week3.csv')
read_csv(input_file)


def student_bar_chart():
    student_list = read_csv('/home/jovyan/python_handin_template/week3.csv')
    for s in student_list:
        plt.bar(name, grade, width=0.5, align='center')
        plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')


def student_bar_chart1():
    student_list = read_csv('/home/jovyan/python_handin_template/week3.csv')
    for student in student_list:
        plt.bar([student.name], [student.datasheet.course.grade], width=0.5, align='center')
        plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')

