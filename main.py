import csv
from file_handler import load_data
from student_operations import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    student_report,
    sort_students,
    export_students_csv,
)


def display_menu():

    print("=" * 40)
    print("    STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Report")
    print("7. Sort Students")
    print("8. Export Students to CSV")
    print("9. Exit")


students = load_data()


while True:

    display_menu()

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        update_student(students)

    elif choice == "5":
        delete_student(students)

    elif choice == "6":
        student_report(students)

    elif choice == "7":
        sort_students(students)

    elif choice == "8":
        export_students_csv(students)

    elif choice == "9":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")