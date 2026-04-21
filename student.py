import json


FILENAME = "student.json"

def main():
    while True:
        print("\n1. Add student\n2. Search student\n3. Update marks\n4. Delete record\n5. Exit\n")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice")
        
        match choice:
            case 1:
                add_student()
            case 2:
                search_student()
            case 3:
                update_marks()
            case 4:
                delete_record()
            case 5:
                print("Exiting...")
                break
            case _:
                print("Invalid choice")
            
def save(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

def load():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_student():
    student_id = input("Student ID: ")
    if not student_id:
        print("Student ID cannot be empty")
        return
    data = load()
    if any(item["student_id"] == student_id for item in data):
        print(f"Student with {student_id} already exist")
    
    name = input("Student name: ")
    try:
        marks = int(input("Marks: "))
    except ValueError:
        print("Invalid value")
        return
    data.append({"student_id":student_id, "name":name, "marks":marks})
    save(data)

def search_student():
    student_id = input("Student ID: ")
    data = load()
    student = next((item for item in data if item["student_id"] == student_id), None)
    if student:
        print("\nStudent details\n")
        print(f"{student_id} | {student["name"]} | {student["marks"]}\n")
    else:
        print("Student not found")

def update_marks():
    student_id = input("Student ID: ")
    data = load()
    student = next((item for item in data if item["student_id"] == student_id), None)
    if student:
        print("\nStudent details\n")
        print(f"{student_id} | {student["name"]} | {student["marks"]}\n")
        try:
            marks = int(input("New marks: "))
        except ValueError:
            print("Invalid marks")
            return
        student["marks"] = marks
        save(data)
        print(f"\nUpdated: {student_id} | {student["name"]} | {student["marks"]}\n")
    else:
        print("Student not found")

def delete_record():
    student_id = input("Student ID: ")
    data = load()
    new_data = [item for item in data if item["student_id" != student_id]]
    if len(new_data) == len(data):
        print("Student not found")
        return
    else:
        save(new_data)
        print("Student deleted successfully")




main()