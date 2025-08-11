students = ["Tebello", "Mamello", "Lubanzi"]

def add_student():
    students.append(input("Enter student name: "))

def get_students():
    for i in range(len(students)):
        print(f"{i + 1}. {students[i]}")


if __name__ == "__main__":
    new_student = add_student()

    get_students()





