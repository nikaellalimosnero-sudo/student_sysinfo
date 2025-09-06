import csv

# Global Variables
students = {}
filename = "student_records.csv"  # file to store student records

# Functions


def grade_avg(grades):
    avg = (lambda g: sum(g) / len(g) if g else 0)(grades)
    return avg


def add_student(student_id, name, age, *grades):
    # Check if student_id already exists
    if student_id in students:
        print("Student ID already exists.")
        return

    # store immutable info  as a tuple
    info = (student_id, name)

    # store all data in dictionary, as key
    students[student_id] = {
        "info": info,
        "age": age,
        "grades": list(grades)  # turn grades into a list
    }
    print(f"Student {name} - {student_id} added successfully.")
    save_to_file()  # Automatically save after adding


def view_students(from_file=False):
    if from_file:
        load_from_file()
        print("\n-----Students from File-----")
    else:
        print("\n-----Students in Memory-----")
    if not students:
        print("No student records found.")
        return

    # Loop through students dictionary to get key-value pairs
    for student_id, details in students.items():
        info = details["info"]
        age = details["age"]
        grades = details["grades"]
        avg_grade = grade_avg(grades)
        # display student info
        print(
            f"ID: {info[0]}, Name: {info[1]}, Age: {age}, Grades: {grades}, Average: {avg_grade:.2f}")
        # nested loop to display each grade
        print("Individual Grades: ")
        for g in grades:
            print(f" - {g}")
        # tuple and dict functions demonstration
        print("Tuple length (ID + Name):", len(info))
        if grades:  # check if grades list is not empty
            print("Max Grade:", max(grades))
            print("Min Grade:", min(grades))
        print("-----")
    # show dictionary keys/values/items outside the loop
    print("All Student IDs (Keys):", students.keys())
    print("All Student Details (Values):", students.values())
    print("All Student Records (Items):", students.items())


def view_single_student(student_id):
    if student_id not in students:
        print("Student ID not found.")
        return
    details = students[student_id]
    info = details["info"]
    age = details["age"]
    grades = details["grades"]
    avg_grade = grade_avg(grades)
    print(
        f"ID: {info[0]}, Name: {info[1]}, Age: {age}, Grades: {grades}, Average: {avg_grade:.2f}")
    if grades:
        print("Max Grade:", max(grades))
        print("Min Grade:", min(grades))


def update_student(student_id, name=None, age=None, grades=None):
    if student_id not in students:
        print("Student ID not found.")
        return
    # any field left as None will not be updated
    if name:
        students[student_id]["info"] = (student_id, name)
    if age:
        students[student_id]["age"] = age
    if grades is not None:  # allow empty list to clear grades
        students[student_id]["grades"] = grades

    print(f"Student {name} - {student_id} updated successfully.")
    save_to_file()  # Automatically save after updating


def delete_student(student_id):
    # delete student record by student_id
    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print("Student ID not found.")
    save_to_file()  # Automatically save after updating


def save_to_file():
    # save student records to a CSV file
    # each row: student_id, name, age, grades (as comma-separated string)
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        for student_id, details in students.items():
            row = [student_id, details["info"][1],
                   details["age"]] + details["grades"]
            writer.writerow(row)
    print(f"Student records saved to {filename}.")


def load_from_file():
    # load student records from a CSV file
    students.clear()  # clear current records
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                student_id, name, age, *grades = row
                age = int(age)
                grades = [int(g) for g in grades]  # convert grades to integers
                students[student_id] = {
                    "info": (student_id, name),
                    "age": age,
                    "grades": grades
                }
    except FileNotFoundError:
        print(f"No existing file {filename} found. Starting fresh.")


# Scope Demonstration
global_var = "I am a global variable"


def scope_demo():
    local_var = "I am a local variable"
    print(global_var)  # Accessing global variable
    print(local_var)   # Accessing local variable


# Main Program
def main():
    load_from_file()  # Load existing records on startup

    while True:
        print("\n===== Student Record Management System =====")
        print("[ 1 ] Add Student")
        print("[ 2 ] Display Students")
        print("[ 3 ] Update Student")
        print("[ 4 ] Delete Student")
        print("[ 5 ] View Single Student")
        print("[ 6 ] Load from File")
        print("[ 7 ] Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":  # Add Student
                student_id = input("Enter Student ID: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                grades_input = input("Enter Grades (comma-separated): ")
                grades = [int(g.strip()) for g in grades_input.split(
                    ",")] if grades_input else []
                add_student(student_id, name, age, *grades)
            case "2":  # Display Students
                sub_choice = input("View from [1] Memory or [2] File? ")
                if sub_choice == "1":
                    view_students(from_file=False)
                elif sub_choice == "2":
                    view_students(from_file=True)
                else:
                    print("Invalid choice.")
            case "3":  # Update Student
                student_id = input("Enter Student ID to update: ")
                name = input("Enter new Name (leave blank to keep current): ")
                age_input = input(
                    "Enter new Age (leave blank to keep current): ")
                grades_input = input(
                    "Enter new Grades (comma-separated, leave blank to keep current): ")
                age = int(age_input) if age_input else None
                grades = [int(g.strip()) for g in grades_input.split(
                    ",")] if grades_input else None
                update_student(student_id, name=name, age=age, grades=grades)
            case "4":  # Delete Student
                student_id = input("Enter Student ID to delete: ")
                delete_student(student_id)
            case "5":  # View Single Student
                student_id = input("Enter Student ID to view: ")
                view_single_student(student_id)
            case "6":  # Load from File
                load_from_file()
            case "7":  # Exit
                print("Exiting program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


# program entry point
if __name__ == "__main__":
    scope_demo()  # demonstrate scope
    main()