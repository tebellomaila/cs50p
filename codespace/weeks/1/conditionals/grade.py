# prompt user for percentage marks
grade = float(input("Enter % marks: "))

# check grade is out of range
if not(0 <= grade <= 100):
    print("Invalid input: expected a number between 0 and 100") # display error message for invalid number  
else:
    # display corresponding grade level for valid grade
    if grade >= 80:
        print("Passed with level 7")
    elif grade >= 70:
        print("Passed with level 6")
    elif grade >= 60:
        print("Passed with level 5")
    elif grade >= 50:
        print("Passed with level 3")
    elif grade >= 40:
        print("Passed with level 2")
    else: 
        print("Failed with level 1")
