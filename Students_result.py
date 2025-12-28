import json

class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def calculate_percentage(self):
        if not self.marks:
            return 0
        total = sum(self.marks.values())
        return total / len(self.marks)

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "Fail"

    def generate_report(self):
        return {
            "Roll No": self.roll_no,
            "Name": self.name,
            "Marks": self.marks,
            "Percentage": self.calculate_percentage(),
            "Grade": self.calculate_grade()
        }


class StudentResultManagement:
    def __init__(self, filename="students_data.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, roll_no, name):
        if roll_no in self.students:
            print("Student already exists!")
            return
        self.students[roll_no] = {
            "name": name,
            "marks": {}
        }
        self.save_data()
        print("Student added successfully.")

    def add_marks(self, roll_no, subject, marks):
        if roll_no not in self.students:
            print("Student not found!")
            return
        self.students[roll_no]["marks"][subject] = marks
        self.save_data()
        print("Marks added successfully.")

    def generate_report(self, roll_no):
        if roll_no not in self.students:
            print("Student not found!")
            return

        student = self.students[roll_no]
        marks = student["marks"]
        percentage = sum(marks.values()) / len(marks) if marks else 0

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "Fail"

        print("\n----- Student Report -----")
        print("Roll No:", roll_no)
        print("Name:", student["name"])
        print("Marks:", marks)
        print("Percentage:", percentage)
        print("Grade:", grade)


def main():
    system = StudentResultManagement()

    while True:
        print("\n1. Add Student")
        print("2. Add Marks")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            system.add_student(roll, name)

        elif choice == "2":
            roll = input("Enter Roll No: ")
            subject = input("Enter Subject: ")
            marks = int(input("Enter Marks: "))
            system.add_marks(roll, subject, marks)

        elif choice == "3":
            roll = input("Enter Roll No: ")
            system.generate_report(roll)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
