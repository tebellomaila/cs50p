""" Get grades for a list of students from dictionary """

def get_grades(student_dict, student_name):
    grade_list = []
    for student in student_dict:
        # Use get() to avoid KeyError
        if student in student_name:
            grade_list += student_dict[student]
    return grade_list

def main():
    # Dictionary mapping student names to grades
    STUDENT_GRADES = {"tebello": "B", "mamello": "A", "mpho": "D"}
    print(STUDENT_GRADES)

    # List of student name to query grades for
    students = ["tebello", "mpho"]
    print(get_grades(STUDENT_GRADES, students))

    # Add student grade to the dictionary
    STUDENT_GRADES["seth"] = "C"
    print(STUDENT_GRADES)

    # Change grade for current student
    STUDENT_GRADES["seth"] = "A"
    print(STUDENT_GRADES)
    
    # Remove student name from the dictionary
    del(STUDENT_GRADES["mpho"])

    # Output all grade results
    print(STUDENT_GRADES)


if __name__ == "__main__":
    main()
