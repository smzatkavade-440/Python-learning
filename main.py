# ================================================================
# SMART STUDENT MANAGEMENT SYSTEM
# Mini Project Using Python OOP
# ================================================================
#
# Concepts Used:
# 1. Classes and Objects
# 2. Constructor (__init__)
# 3. Encapsulation
# 4. Inheritance
# 5. Abstraction
# 6. Methods
# 7. Decorators
# 8. Callback Functions
# 9. Closures
# 10. Lists and Dictionaries
# 11. Exception Handling
# ================================================================

from abc import ABC, abstractmethod


# ================================================================
# DECORATOR
# ================================================================

def log_action(func):
    """
    Decorator used to display which operation is being performed.
    """

    def wrapper(*args, **kwargs):
        print("\n----------------------------------------")
        print("Operation started:", func.__name__)
        print("----------------------------------------")

        result = func(*args, **kwargs)

        print("----------------------------------------")
        print("Operation completed:", func.__name__)
        print("----------------------------------------")

        return result

    return wrapper


# ================================================================
# ABSTRACT CLASS
# ================================================================

class Person(ABC):
    """
    Abstract base class representing a person.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_details(self):
        """
        Abstract method.
        Child classes must implement this method.
        """
        pass


# ================================================================
# STUDENT CLASS
# ================================================================

class Student(Person):
    """
    Student class inherited from Person.
    """

    total_students = 0

    def __init__(self, student_id, name, age, branch, semester):
        super().__init__(name, age)

        self.student_id = student_id
        self.branch = branch
        self.semester = semester

        # Encapsulation
        self.__marks = {}

        Student.total_students += 1

    # ------------------------------------------------------------
    # Add marks
    # ------------------------------------------------------------

    def add_marks(self, subject, marks):

        if 0 <= marks <= 100:
            self.__marks[subject] = marks
            print(f"Marks added successfully for {subject}.")
        else:
            print("Marks must be between 0 and 100.")

    # ------------------------------------------------------------
    # Get marks
    # ------------------------------------------------------------

    def get_marks(self):
        return self.__marks.copy()

    # ------------------------------------------------------------
    # Calculate percentage
    # ------------------------------------------------------------

    def calculate_percentage(self):

        if len(self.__marks) == 0:
            return 0

        total = sum(self.__marks.values())
        number_of_subjects = len(self.__marks)

        return total / number_of_subjects

    # ------------------------------------------------------------
    # Calculate grade
    # ------------------------------------------------------------

    def calculate_grade(self):

        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"

        elif percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"

        elif percentage >= 60:
            return "C"

        elif percentage >= 50:
            return "D"

        elif percentage >= 40:
            return "E"

        else:
            return "F"

    # ------------------------------------------------------------
    # Display student details
    # ------------------------------------------------------------

    def display_details(self):

        print("\n========================================")
        print("           STUDENT DETAILS")
        print("========================================")

        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Branch     :", self.branch)
        print("Semester   :", self.semester)

        print("\nSubjects & Marks:")

        if len(self.__marks) == 0:
            print("No marks available.")

        else:
            for subject, marks in self.__marks.items():
                print(f"{subject:<20} : {marks}")

        print("\nPercentage :", round(self.calculate_percentage(), 2), "%")
        print("Grade      :", self.calculate_grade())

        print("========================================")


# ================================================================
# TEACHER CLASS
# ================================================================

class Teacher(Person):
    """
    Teacher class inherited from Person.
    """

    def __init__(self, teacher_id, name, age, department):
        super().__init__(name, age)

        self.teacher_id = teacher_id
        self.department = department

    def display_details(self):

        print("\n========================================")
        print("           TEACHER DETAILS")
        print("========================================")

        print("Teacher ID :", self.teacher_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Department :", self.department)

        print("========================================")


# ================================================================
# COURSE CLASS
# ================================================================

class Course:

    def __init__(self, course_id, course_name, teacher):

        self.course_id = course_id
        self.course_name = course_name
        self.teacher = teacher

    def display_course(self):

        print("\n----------------------------------------")
        print("Course ID   :", self.course_id)
        print("Course Name :", self.course_name)
        print("Teacher     :", self.teacher)
        print("----------------------------------------")


# ================================================================
# STUDENT MANAGEMENT SYSTEM
# ================================================================

class StudentManagementSystem:

    def __init__(self):

        self.students = []
        self.teachers = []
        self.courses = []

    # ============================================================
    # ADD STUDENT
    # ============================================================

    @log_action
    def add_student(self):

        print("\n========== ADD STUDENT ==========")

        student_id = input("Enter Student ID: ")

        # Check duplicate ID
        for student in self.students:

            if student.student_id == student_id:
                print("Student ID already exists.")
                return

        name = input("Enter Student Name: ")

        try:
            age = int(input("Enter Age: "))
            semester = int(input("Enter Semester: "))

        except ValueError:

            print("Please enter numbers for age and semester.")
            return

        branch = input("Enter Branch: ")

        student = Student(
            student_id,
            name,
            age,
            branch,
            semester
        )

        self.students.append(student)

        print("\nStudent added successfully!")

    # ============================================================
    # ADD MARKS
    # ============================================================

    @log_action
    def add_student_marks(self):

        student = self.find_student()

        if student is None:
            return

        print("\n========== ADD MARKS ==========")

        subject = input("Enter Subject Name: ")

        try:
            marks = float(input("Enter Marks: "))

        except ValueError:

            print("Invalid marks.")
            return

        student.add_marks(subject, marks)

    # ============================================================
    # FIND STUDENT
    # ============================================================

    def find_student(self):

        student_id = input("Enter Student ID: ")

        for student in self.students:

            if student.student_id == student_id:
                return student

        print("Student not found.")

        return None

    # ============================================================
    # DISPLAY ONE STUDENT
    # ============================================================

    @log_action
    def display_student(self):

        student = self.find_student()

        if student is not None:
            student.display_details()

    # ============================================================
    # DISPLAY ALL STUDENTS
    # ============================================================

    @log_action
    def display_all_students(self):

        if len(self.students) == 0:

            print("\nNo students registered.")

            return

        print("\n========== ALL STUDENTS ==========")

        for student in self.students:

            print(
                f"ID: {student.student_id} | "
                f"Name: {student.name} | "
                f"Branch: {student.branch} | "
                f"Semester: {student.semester}"
            )

    # ============================================================
    # DELETE STUDENT
    # ============================================================

    @log_action
    def delete_student(self):

        student = self.find_student()

        if student is None:
            return

        self.students.remove(student)

        print("Student deleted successfully.")

    # ============================================================
    # ADD TEACHER
    # ============================================================

    @log_action
    def add_teacher(self):

        print("\n========== ADD TEACHER ==========")

        teacher_id = input("Enter Teacher ID: ")
        name = input("Enter Teacher Name: ")

        try:
            age = int(input("Enter Age: "))

        except ValueError:

            print("Invalid age.")
            return

        department = input("Enter Department: ")

        teacher = Teacher(
            teacher_id,
            name,
            age,
            department
        )

        self.teachers.append(teacher)

        print("Teacher added successfully.")

    # ============================================================
    # DISPLAY TEACHERS
    # ============================================================

    @log_action
    def display_teachers(self):

        if len(self.teachers) == 0:

            print("\nNo teachers available.")

            return

        print("\n========== TEACHERS ==========")

        for teacher in self.teachers:

            teacher.display_details()

    # ============================================================
    # ADD COURSE
    # ============================================================

    @log_action
    def add_course(self):

        print("\n========== ADD COURSE ==========")

        course_id = input("Enter Course ID: ")
        course_name = input("Enter Course Name: ")
        teacher = input("Enter Teacher Name: ")

        course = Course(
            course_id,
            course_name,
            teacher
        )

        self.courses.append(course)

        print("Course added successfully.")

    # ============================================================
    # DISPLAY COURSES
    # ============================================================

    @log_action
    def display_courses(self):

        if len(self.courses) == 0:

            print("\nNo courses available.")

            return

        print("\n========== COURSES ==========")

        for course in self.courses:

            course.display_course()

    # ============================================================
    # CALLBACK FUNCTION EXAMPLE
    # ============================================================

    def process_students(self, callback):

        result = []

        for student in self.students:

            if callback(student):

                result.append(student)

        return result

    # ============================================================
    # SEARCH STUDENTS BY BRANCH
    # ============================================================

    @log_action
    def search_by_branch(self):

        branch = input("Enter Branch: ")

        # Callback function
        def branch_filter(student):

            return student.branch.lower() == branch.lower()

        matching_students = self.process_students(branch_filter)

        if len(matching_students) == 0:

            print("No students found.")

            return

        print("\nStudents from", branch)

        for student in matching_students:

            print(
                student.student_id,
                "-",
                student.name
            )

    # ============================================================
    # SEARCH STUDENTS BY GRADE
    # ============================================================

    @log_action
    def search_by_grade(self):

        grade = input("Enter Grade: ")

        # Callback function
        def grade_filter(student):

            return student.calculate_grade().upper() == grade.upper()

        matching_students = self.process_students(grade_filter)

        if len(matching_students) == 0:

            print("No students found.")

            return

        print("\nStudents with grade", grade)

        for student in matching_students:

            print(
                student.student_id,
                "-",
                student.name,
                "-",
                student.calculate_percentage()
            )

    # ============================================================
    # CLOSURE EXAMPLE
    # ============================================================

    def create_percentage_checker(self, minimum_percentage):

        def checker(student):

            return student.calculate_percentage() >= minimum_percentage

        return checker

    # ============================================================
    # FIND HIGH PERFORMING STUDENTS
    # ============================================================

    @log_action
    def high_performance_students(self):

        try:

            minimum = float(
                input("Enter minimum percentage: ")
            )

        except ValueError:

            print("Invalid percentage.")

            return

        # Closure
        checker = self.create_percentage_checker(minimum)

        students = self.process_students(checker)

        if len(students) == 0:

            print("No students found.")

            return

        print(
            f"\nStudents with percentage >= {minimum}"
        )

        for student in students:

            print(
                student.student_id,
                "-",
                student.name,
                "-",
                round(student.calculate_percentage(), 2),
                "%"
            )

    # ============================================================
    # PROJECT STATISTICS
    # ============================================================

    @log_action
    def statistics(self):

        print("\n========== SYSTEM STATISTICS ==========")

        print(
            "Total Students :",
            len(self.students)
        )

        print(
            "Total Teachers :",
            len(self.teachers)
        )

        print(
            "Total Courses  :",
            len(self.courses)
        )

        if len(self.students) > 0:

            percentages = []

            for student in self.students:

                percentages.append(
                    student.calculate_percentage()
                )

            average = sum(percentages) / len(percentages)

            print(
                "Average Student Percentage :",
                round(average, 2),
                "%"
            )

        else:

            print(
                "Average Student Percentage : No data"
            )


# ================================================================
# SAMPLE DATA
# ================================================================

def load_sample_data(system):

    # Students

    s1 = Student(
        "S001",
        "Satish",
        19,
        "VLSI",
        3
    )

    s1.add_marks("Python", 92)
    s1.add_marks("Digital Electronics", 88)
    s1.add_marks("VLSI Design", 91)
    s1.add_marks("Embedded Systems", 85)

    system.students.append(s1)


    s2 = Student(
        "S002",
        "Rahul",
        20,
        "VLSI",
        3
    )

    s2.add_marks("Python", 75)
    s2.add_marks("Digital Electronics", 78)
    s2.add_marks("VLSI Design", 72)
    s2.add_marks("Embedded Systems", 80)

    system.students.append(s2)


    s3 = Student(
        "S003",
        "Amit",
        19,
        "Computer",
        3
    )

    s3.add_marks("Python", 65)
    s3.add_marks("Digital Electronics", 60)
    s3.add_marks("VLSI Design", 68)
    s3.add_marks("Embedded Systems", 70)

    system.students.append(s3)


    # Teacher

    teacher = Teacher(
        "T001",
        "Prof. Sharma",
        40,
        "Electronics Engineering"
    )

    system.teachers.append(teacher)


    # Course

    course = Course(
        "C001",
        "Python Programming",
        "Prof. Sharma"
    )

    system.courses.append(course)


# ================================================================
# MAIN MENU
# ================================================================

def main():

    system = StudentManagementSystem()

    # Load demonstration data
    load_sample_data(system)

    while True:

        print("\n")
        print("================================================")
        print("       SMART STUDENT MANAGEMENT SYSTEM")
        print("================================================")

        print("1.  Add Student")
        print("2.  Add Student Marks")
        print("3.  Display Student")
        print("4.  Display All Students")
        print("5.  Delete Student")

        print("6.  Add Teacher")
        print("7.  Display Teachers")

        print("8.  Add Course")
        print("9.  Display Courses")

        print("10. Search Students by Branch")
        print("11. Search Students by Grade")
        print("12. Find High Performing Students")

        print("13. System Statistics")

        print("0.  Exit")

        print("================================================")

        choice = input("Enter your choice: ")

        # --------------------------------------------------------
        # MENU OPTIONS
        # --------------------------------------------------------

        if choice == "1":

            system.add_student()

        elif choice == "2":

            system.add_student_marks()

        elif choice == "3":

            system.display_student()

        elif choice == "4":

            system.display_all_students()

        elif choice == "5":

            system.delete_student()

        elif choice == "6":

            system.add_teacher()

        elif choice == "7":

            system.display_teachers()

        elif choice == "8":

            system.add_course()

        elif choice == "9":

            system.display_courses()

        elif choice == "10":

            system.search_by_branch()

        elif choice == "11":

            system.search_by_grade()

        elif choice == "12":

            system.high_performance_students()

        elif choice == "13":

            system.statistics()

        elif choice == "0":

            print("\nThank you for using")
            print("Smart Student Management System!")

            break

        else:

            print("\nInvalid choice.")
            print("Please select a valid option.")


# ================================================================
# PROGRAM START
# ================================================================

if __name__ == "__main__":

    main()
