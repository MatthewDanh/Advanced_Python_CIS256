"""
A class that represents a grade tracker for a student.

Attributes:
    name (str): The name of the student.
    points_earned (float): The total points earned by the student.
    points_possible (float): The total points possible for the student.

Methods:
    get_percentage(): Calculates the percentage of points earned.
    get_letter_grade(): Determines the letter grade based on the percentage.
    add_assignment_score(points_earned, points_possible): Adds points earned and points possible for an assignment.
    add_extra_credit(points): Adds extra credit points to the total points earned.
    show_grade(): Displays the student's name, points earned, points possible, percentage, and letter grade.
"""
class StudentGrade:
    def __init__(self, name, points_earned, points_possible):
        self.__name = name
        self.__points_earned = points_earned
        self.__points_possible = points_possible

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def points_earned(self):
        return self.__points_earned

    @points_earned.setter
    def points_earned(self, value):
        if value < 0:
            raise ValueError("Points earned cannot be negative")
        self.__points_earned = value

    @property
    def points_possible(self):
        return self.__points_possible

    @points_possible.setter
    def points_possible(self, value):
        if value < 0:
            raise ValueError("Points possible cannot be negative")
        self.__points_possible = value

    @property
    def get_percentage(self):
            return (self.__points_earned / self.__points_possible) * 100

    def get_letter_grade(self):
            percentage = self.get_percentage
            if percentage >= 90:
                return 'A'
            elif percentage >= 80:
                return 'B'
            elif percentage >= 70:
                return 'C'
            elif percentage >= 60:
                return 'D'
            else:
                return 'F'

    def add_assignment_score(self, points_earned, points_possible):
        self.__points_earned += points_earned
        self.__points_possible += points_possible

    def add_extra_credit(self, points):
        self.__points_earned += points
        # Note: Adding extra credit should not increase points possible, based on previous assumption.
        
    def show_grade(self):
            percentage = self.get_percentage
            letter_grade = self.get_letter_grade()
            return f"{self.__name} earned {self.__points_earned} out of {self.__points_possible} points, which is {percentage:.2f}% and a letter grade of {letter_grade}"

my_grade = StudentGrade("Matthew", 480, 500)
print(my_grade.get_percentage)

# Adding an assignment with 7 points earned out of 10 possible
my_grade.add_assignment_score(7, 10)

# Adding extra credit for 15 points
my_grade.add_extra_credit(15)

# Print the grade table
def print_grade_table(grade_trackers):
    header = f"{'Name':<10} | {'Earned':<10} | {'Possible':<10} | {'Percentage':<12} | {'Grade':<5}"
    divider = "-" * len(header)
    print(f"{header}\n{divider}")
    for grade_tracker in grade_trackers:
        # Accessing get_percentage as a property, not as a method
        percentage = grade_tracker.get_percentage  # Correctly accessing the property
        data = f"{grade_tracker.name:<10} | {grade_tracker.points_earned:<10} | {grade_tracker.points_possible:<10} | {percentage:<12.2f}% | {grade_tracker.get_letter_grade():<5}"
        print(data)

# Create grade trackers for three students
student1 = StudentGrade("Lindsey", 400, 500)
student2 = StudentGrade("Matthew", 480, 500)
student3 = StudentGrade("John", 480, 500)

# Create a list of grade trackers
students = [student1, student2, student3]

# Print the grade table
print_grade_table(students)

