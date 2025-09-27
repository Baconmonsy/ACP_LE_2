class Student:
    def __init__(self, student_id, name, email, grades=None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.grades = grades if grades else {}

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Email: {self.email}"

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        gpa = 0
        for score in self.grades.values():
            if score >= 90:
                gpa += 4.0
            elif score >= 80:
                gpa += 3.0
            elif score >= 70:
                gpa += 2.0
            elif score >= 60:
                gpa += 1.0
            else:
                gpa += 0.0
        return round(gpa / len(self.grades), 2)


class StudentRecords:
    def __init__(self):
        self.students = {}

    def add_student(self, sid, name, email, grades=None):
        student = Student(sid, name, email, grades)
        self.students[sid] = student
        return student


if _name_ == "_main_":
    records = StudentRecords()

    
    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    email = input("Enter Email: ")

   
    student = records.add_student(id, name, email, {})

    
    while True:
        subj = input("\nEnter subject: ")
        if subj == "":
            break

        try:
            grade = float(input("Enter grade: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        student.grades[subj] = grade

        print("\nRecord Updated!")
        print(student)
        print("Subjects and Grades (with GPA):")
        for subject, score in student.grades.items():
            if score >= 90:
                gpa = 4.0
            elif score >= 80:
                gpa = 3.0
            elif score >= 70:
                gpa = 2.0
            elif score >= 60:
                gpa = 1.0
            else:
                gpa = 0.0
            print(f"  {subject}: {score} → {gpa}")

        print(f"Updated Overall GPA: {student.calculate_gpa():.2f}")
