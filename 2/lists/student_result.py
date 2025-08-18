""" Dummy data and list of students results """

tebello = ["tebello", ["tests", [62, 78, 56]], ["exams", [74, 48]]]
thabiso = ["thabiso", ["tests", [42, 69, 38]], ["exams", [63, 84]]]
luke = ["luke", ["tests", [78, 82, 65]], ["exams", [89, 94]]]
seth = ["seth", ["tests", [84, 67, 79]], ["exams", [82, 80]]]

""" A list of student records to search """
STUDENTS =  [tebello, thabiso, luke, seth]

""" Get grade results for student name to search for """

def get_student_results(name, category, student_list):
    # Search through each student in the list for name match
    for student in student_list:
        if student[0] == name:
            # Search for the student's category results
            for result in student[1:]:
                if result[0] == category:
                    return f"{category.title()} Results {result[1]}" # Results found for student
            else:

                return f"Results not found"
    
    return "Student not found"


def main():
    print(get_student_results("seth", "exams", STUDENTS))    
    print(get_student_results("tebello", "tests", STUDENTS))
    print(get_student_results("thabiso", "projects", STUDENTS))
    print(get_student_results("neo", "exams", STUDENTS))



if __name__ == "__main__":
    main()
