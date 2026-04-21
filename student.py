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






main()