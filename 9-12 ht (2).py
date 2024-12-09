class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    def student_info(self):
        print(f"Student Name: {self.name}, Course: {self.course}")
class StudentAthlete(Student):
    def __init__(self, name, course, sport):
        super().__init__(name, course)
        self.sport = sport
        def display_athlete_info(self):
        print(f"Student Name: {self.name}, Course: {self.course}, Sport: {self.sport}")
athlete = StudentAthlete(name="John Doe", course="Computer Science", sport="Basketball")
athlete.student_info()
athlete.display_athlete_info()
