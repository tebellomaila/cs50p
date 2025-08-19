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
    print(STUDENT_GRADES)

    # List of student name to query grades for
    students = ["tebello", "mpho"]
    print(get_grades(STUDENT_GRADES, ["tebello", "mpho"]))

    # Add student grade to the dictionary
    STUDENT_GRADES["seth"] = "C"
    print(get_grades(STUDENT_GRADES, ["seth"]))

    # Change grade for current student
    STUDENT_GRADES["seth"] = "A"
    print(get_grades(STUDENT_GRADES, ["seth"]))
    
    # Remove student name from the dictionary
    del(STUDENT_GRADES["mpho"])

    # Output all grade results
    print(STUDENT_GRADES)


if __name__ == "__main__":
    main()
