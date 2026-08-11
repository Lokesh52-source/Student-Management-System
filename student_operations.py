import csv
from file_handler import save_data
from validation import (
    get_valid_roll_no,
    get_valid_name,
    get_valid_age,
    get_valid_course,
    get_valid_marks
)


def add_student(students):

    roll_no = get_valid_roll_no("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Roll Number already exists!")
            return

    name = get_valid_name("Enter Name: ")
    age = get_valid_age("Enter Age: ")
    course = get_valid_course("Enter Course: ")
    marks = get_valid_marks("Enter Marks: ")

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_data(students)

    print("Student Added Successfully!")


def view_students(students):

    if len(students) == 0:
        print("No students found.")
        return

    print("-" * 75)

    print(
        f"{'Roll No':<10}"
        f"{'Name':<15}"
        f"{'Age':<8}"
        f"{'Course':<20}"
        f"{'Marks':<10}"
    )

    print("-" * 75)

    for student in students:
        print(
            f"{student['roll_no']:<10}"
            f"{student['name']:<15}"
            f"{student['age']:<8}"
            f"{student['course']:<20}"
            f"{student['marks']:<10}"
        )

    print("-" * 75)

def print_student(student):

    print("\nStudent Found")
    print("-" * 40)

    print(f"Roll No : {student['roll_no']}")
    print(f"Name    : {student['name']}")
    print(f"Age     : {student['age']}")
    print(f"Course  : {student['course']}")
    print(f"Marks   : {student['marks']}")

    print("-" * 40)


def search_student(students):

    print("\n===== SEARCH STUDENT =====")
    print("1. Search by Roll Number")
    print("2. Search by Name")
    print("3. Search by Course")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":

        roll_no = get_valid_roll_no("Enter Roll Number: ")

        for student in students:
            if student["roll_no"] == roll_no:
                print_student(student)
                return

        print("Student not found.")

    elif choice == "2":

        name = get_valid_name("Enter Student Name: ").lower()

        found = False

        for student in students:
            if student["name"].lower() == name:
                print_student(student)
                found = True

        if not found:
            print("Student not found.")

    elif choice == "3":

        course = get_valid_course("Enter Course: ").lower()

        found = False

        for student in students:
            if student["course"].lower() == course:
                print_student(student)
                found = True

        if not found:
            print("No students found for this course.")

    else:
        print("Invalid choice.")

def sort_students(students):

    if len(students) == 0:
        print("No students available.")
        return

    print("\n===== SORT STUDENTS =====")
    print("1. Sort by Roll Number")
    print("2. Sort by Name")
    print("3. Sort by Age")
    print("4. Sort by Marks")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":

        sorted_students = sorted(
            students,
            key=lambda student: student["roll_no"]
        )

    elif choice == "2":

        sorted_students = sorted(
            students,
            key=lambda student: student["name"].lower()
        )

    elif choice == "3":

        sorted_students = sorted(
            students,
            key=lambda student: student["age"]
        )

    elif choice == "4":

        sorted_students = sorted(
            students,
            key=lambda student: student["marks"],
            reverse=True
        )

    else:
        print("Invalid choice.")
        return

    print("\nSorted Students")
    print("-" * 75)

    print(
        f"{'Roll No':<10}"
        f"{'Name':<15}"
        f"{'Age':<8}"
        f"{'Course':<20}"
        f"{'Marks':<10}"
    )

    print("-" * 75)

    for student in sorted_students:

        print(
            f"{student['roll_no']:<10}"
            f"{student['name']:<15}"
            f"{student['age']:<8}"
            f"{student['course']:<20}"
            f"{student['marks']:<10}"
        )

    print("-" * 75)


def update_student(students):

    roll_no = get_valid_roll_no("Enter Roll Number to Update: ")

    for student in students:

        if student["roll_no"] == roll_no:

            print("\nCurrent Details")
            print("-" * 30)
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            print(f"Marks  : {student['marks']}")

            print("\nEnter New Details")

            student["name"] = get_valid_name("Enter New Name: ")
            student["age"] = get_valid_age("Enter New Age: ")
            student["course"] = get_valid_course("Enter New Course: ")
            student["marks"] = get_valid_marks("Enter New Marks: ")

            save_data(students)

            print("Student Updated Successfully!")
            return

    print("Student not found.")


def delete_student(students):

    roll_no = get_valid_roll_no("Enter Roll Number to Delete: ")

    for student in students:

        if student["roll_no"] == roll_no:

            print("\nStudent Found")
            print("-" * 40)
            print(f"Roll No : {student['roll_no']}")
            print(f"Name    : {student['name']}")
            print(f"Age     : {student['age']}")
            print(f"Course  : {student['course']}")
            print(f"Marks   : {student['marks']}")
            print("-" * 40)

            confirmation = input(
                "Are you sure you want to delete this student? (y/n): "
            ).lower()

            if confirmation == "y":

                students.remove(student)
                save_data(students)

                print("Student Deleted Successfully!")

            else:
                print("Delete operation cancelled.")

            return

    print("Student not found.")


def student_report(students):

    if len(students) == 0:
        print("No students available.")
        return

    total_students = len(students)

    highest = max(student["marks"] for student in students)
    lowest = min(student["marks"] for student in students)

    total_marks = sum(student["marks"] for student in students)
    average = total_marks / total_students

    top_student = max(
        students,
        key=lambda student: student["marks"]
    )

    pass_count = 0

    for student in students:
        if student["marks"] >= 35:
            pass_count += 1

    fail_count = total_students - pass_count

    print("\n========== STUDENT REPORT ==========")
    print(f"Total Students : {total_students}")
    print(f"Highest Marks  : {highest}")
    print(f"Lowest Marks   : {lowest}")
    print(f"Average Marks  : {average:.2f}")
    print(f"Top Scorer     : {top_student['name']}")
    print(f"Pass Students  : {pass_count}")
    print(f"Fail Students  : {fail_count}")
    print("====================================")

def export_students_csv(students):

    if len(students) == 0:
        print("No students available to export.")
        return

    with open("students.csv", "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "roll_no",
                "name",
                "age",
                "course",
                "marks"
            ]
        )

        writer.writeheader()
        writer.writerows(students)

    print("Student data exported successfully to students.csv")