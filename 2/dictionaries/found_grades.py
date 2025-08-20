""" A dictionary of student records to search """

STUDENTS = { 
            "tebello": {"id": "214737600", "tests": [62,78,56], "exams": [74,48]},
            "thabiso": {"id": "213345809", "exams": [63,84]},
            "mamello": {"id": "214534067", "tests": [78,82,65], "exams": [89,94]},
            "seth": {"id": "219600562", "tests": [84,67,79], "exams": [82,80]},
            "tshepo": {"id": "219600874", "tests": [], "exams":[]}
}

""" Validate student exists and return True if student has grade results otherwise False """
def grades_found(student_name, student_dict):
    # Search the student name in the list of dictionaries
    if student_name not in student_dict:
        return "Student not found"
    # Get student record
    student = student_dict[student_name]
    tests_found = "tests" in student and len(student["tests"]) > 0
    exams_found = "exams" in student and len(student["exams"]) > 0
    return tests_found or exams_found


def main():
    # Test cases
    print(grades_found("tebello", STUDENTS))
    print(grades_found("thabiso", STUDENTS))
    print(grades_found("tshepo", STUDENTS))
    print(grades_found("lubanzi", STUDENTS))



if __name__ == "__main__":
    main()
