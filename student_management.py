import json

# Load data from JSON file
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []


# Save data to JSON file
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")
    email = input("Enter Email: ")
    cgpa = float(input("Enter CGPA: "))

    student = {
        "id": student_id,
        "name": name,
        "department": department,
        "semester": semester,
        "email": email,
        "cgpa": cgpa
    }

    students.append(student)
    save_data()

    print("\n✅ Student Added Successfully!")


def view_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No Students Found!")
        return

    for student in students:
        print("-" * 40)
        print(f"ID         : {student['id']}")
        print(f"Name       : {student['name']}")
        print(f"Department : {student['department']}")
        print(f"Semester   : {student['semester']}")
        print(f"Email      : {student['email']}")
        print(f"CGPA       : {student['cgpa']}")


def search_student():
    print("\n--- Search Student ---")

    search_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found!")
            print(student)
            return

    print("Student Not Found!")


def update_student():
    print("\n--- Update Student ---")

    update_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == update_id:

            student["name"] = input("New Name: ")
            student["department"] = input("New Department: ")
            student["semester"] = input("New Semester: ")
            student["email"] = input("New Email: ")
            student["cgpa"] = float(input("New CGPA: "))

            save_data()

            print("✅ Student Updated Successfully!")
            return

    print("Student Not Found!")


def delete_student():
    print("\n--- Delete Student ---")

    delete_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)

            save_data()

            print("✅ Student Deleted Successfully!")
            return

    print("Student Not Found!")


def show_top_student():
    print("\n--- Top Student ---")

    if len(students) == 0:
        print("No Students Available!")
        return

    top_student = max(students, key=lambda student: student["cgpa"])

    print(f"Name : {top_student['name']}")
    print(f"CGPA : {top_student['cgpa']}")


def student_count():
    print("\n--- Statistics ---")
    print(f"Total Students: {len(students)}")


while True:

    print("\n" + "=" * 45)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Top Student")
    print("7. Student Count")
    print("8. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        show_top_student()

    elif choice == "7":
        student_count()

    elif choice == "8":
        print("\nThank You For Using The System!")
        break

    else:
        print("Invalid Choice!")
