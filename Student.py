class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name)
        self.email = email
        self.grades = dict(grades) if grades is not None else {}
        self.courses = set(courses) if courses is not None else set()
        
    def __str__(self):
        sid, name = self.id_name
        grades_str = ", ".join(f"{sub}: {score}" for sub, score in self.grades.items()) or "No grades"
        courses_str = ", ".join(sorted(self.courses)) or "No courses"
        return (
            f"Student ID: {sid}\n"
            f"Name: {name}\n"
            f"Email: {self.email}\n"
            f"Grades: {grades_str}\n"
            f"Courses: {courses_str}"
        )
