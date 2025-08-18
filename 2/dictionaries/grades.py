""" Get grades for a list of students from dictionary """

def get_grades(grade_dict, student_names):
    grade_list = []
    for student in student_names:
        # Use get() to avoid KeyError
        grade_list.append(grade_dict[student])
    return grade_list

def main():
    # Dictionary mapping student names to grades
    STUDENT_GRADES = {"tebello": "B", "mamello": "A", "mpho": "D"}

    # List of student name to query grades for
    students = ["tebello", "mpho"]
    
    # Output the results
    print(get_grades(STUDENT_GRADES, ["tebello", "mpho"]))
    print(get_grades(STUDENT_GRADES, ["seth"]))


if __name__ == "__main__":
    main()


