""" A dictionary of student records to search """

STUDENTS = {
        "214737600": {"name": "tebello", "tests": [62,78,56], "exams": [74,48]},
        "213345809": {"name": "thabiso", "exams": [63,84]},
        "214534067": {"name": "mamello", "tests": [78,82,65], "exams": [89,94]},
        "219600562": {"name": "seth", "tests": [84,67,79], "exams": [82,80]},
        "219600874": {"name": "tshepo", "tests": [], "exams":[]}
}

""" Get the average of all student's grade results for a specified grade result """
def get_average_grades(grade, student_dict):
    grade_list = []
    # Iterate through each student records and add grade result to the list
    for student in student_dict.keys():
        grade_list += student_dict[student][grade]
    # Calculates the average of all student grade results
    return sum(grade_list)/len(grade_list)
    

def main():
    # Test cases
    average_grades = (get_average_grades("tests", STUDENTS))
    print(f"Average Grade: {average_grades}")


if __name__ == "__main__":
    main()
