""" Dummy data and dictionary of student results """

tebello = {"name": "tebello", "id": "214737600", "tests": [62,78,56], "exams": [74,48]}
thabiso = {"name": "thabiso", "id": "213345809", "exams": [63,84]}
mamello = {"name": "mamello", "id": "214534067", "tests": [78,82,65], "exams": [89,94]}
seth = {"name": "seth", "id": "219600562", "tests": [84,67,79], "exams": [82,80]}
tshepo = {"name": "tshepo", "id": "219600874", "tests": [], "exams":[]}


""" A list of student records to search """
STUDENTS = [tshepo, tebello, mamello, seth, thabiso]

""" Find grade results and return True if grade results exist otherwise False """
def grades_found(student_name, student_list):
    # Search the student name in the list of dictionaries
    for student in student_list:
        if student["name"] == student_name:
            return True if ("tests" in student and len(student["tests"]) > 0) or ("exams" in student and len(student["exams"]) >0) else False
    return "Student not found"


def main():
    # Test cases
    print(grades_found("tebello", STUDENTS))
    print(grades_found("thabiso", STUDENTS))
    print(grades_found("tshepo", STUDENTS))
    print(grades_found("lubanzi", STUDENTS))



if __name__ == "__main__":
    main()
