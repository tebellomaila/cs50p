""" Dummy data and list of students results """

tebello = ["tebello", ["tests", [62, 78, 56]], ["exams", [74, 48]]]
thabiso = ["thabiso", ["tests", [42, 69, 38]], ["exams", [63, 84]]]
luke = ["luke", ["tests", [78, 82, 65]], ["exams", [89, 94]]]
seth = ["seth", ["tests", [84, 67, 79]], ["exams", [82, 80]]]

""" A list of student records to search """
STUDENTS =  [tebello, thabiso, luke, seth]

""" Get grade results for student name to search for """

def get_student_results(student_name, student_grade, student_list):
    # Search through each student in the list for name match
    for student in student_list:
        if student[0] == student_name:
            output  = f"Student: {student_name.title()}\n"
            output += f"{'-' * 30}\n"
            # Search for the student's grade results
            for result in student[1:]:
                if result[0] == student_grade:
                    output += f"{student_grade.title()} Results: {result[1]}\n" 
                    return output   # Results found for student
            else:
                output += f"Results not found\n"
                return output
    
    return "Student not found\n"


def main():
    print(get_student_results("seth", "exams", STUDENTS))    
    print(get_student_results("tebello", "tests", STUDENTS))
    print(get_student_results("thabiso", "projects", STUDENTS))
    print(get_student_results("neo", "exams", STUDENTS))



if __name__ == "__main__":
    main()
