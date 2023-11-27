class University:
    def __init__(self, name):
        self.uni_name = name

    def show_details(self):
        print(f"Name of the university is {self.uni_name}")


class Course(University):
    def __init__(self, name, course_name):
        super().__init__(name)
        self.course_name = course_name

    def show_details_C(self):
        print(f"Course I choose is {self.course_name} from {self.uni_name}")


class Branch(University):
    def __init__(self, name, branch_name):
        super().__init__(name)
        self.branch_name = branch_name

    def show_details_B(self):
        print(f"Branch I choose is {self.branch_name} from {self.uni_name}")


class Student(Course, Branch):
    def __init__(self, name, course_name, branch_name, student_name):
        super().__init__(name,course_name)
        self.branch_name=branch_name
        self.student_name = student_name

    def show_details_S(self):
        print(f"I am {self.student_name} from {self.uni_name} studying {self.branch_name} in {self.course_name}")


# Creating instances
university_1 = University("Gurunanak University")
university_1.show_details()

course_1 = Course("Gurunanak University", "Engineering")
course_1.show_details_C()

branch_1 = Branch("Gurunanak University","Electrical")
branch_1.show_details_B()

student_1 = Student("Gurunanak University", "Engineering", "Electrical", "Gowtham")
student_1.show_details_S()
