class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def student_info(self):
        print(f"----\nStudent name:{self.name}\nAge: {self.age}\nGrades{self.grades}\n----")
    def calc_avg(self):
        if self.grades:
            return sum(self.grades)/ len(self.grades)
        return 0
    
class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.student_info()
            print("Average grades: {}".format(student.calc_avg()))

    def calc_overall_avg_grade(self):
        total_grades = []
        for student in self.students:
            total_grades.extend(student.grades)
        if total_grades:
            return sum(total_grades)/len(total_grades)   
        return 0
    
def main():
    stu1 = Student("Esam", 25, [1,2,3,4,5])
    stu2 = Student("Hawa", 26, [3,5,6])
    stu3 = Student("Gamal", 54, [3,2,4,4,5])
    
    database = StudentDatabase()
    database.add_student(stu1)
    database.add_student(stu2)
    database.add_student(stu3)


    database.display_all_students()

    print(database.calc_overall_avg_grade())

    print(stu1.grades)
 
main()