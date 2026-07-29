# Student Result Management System

def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "Fail"


def calculate_average(marks):
    return sum(marks) / len(marks)


def save_result(name, marks, average, grade):
    with open("result.txt", "w") as file:
        file.write("Student Result\n")
        file.write("-----------------\n")
        file.write(f"Name: {name}\n")
        file.write(f"Marks: {marks}\n")
        file.write(f"Average: {average:.2f}\n")
        file.write(f"Grade: {grade}\n")

    print("Result saved to result.txt")


try:
    print("=== Student Result Management System ===")

    name = input("Enter student name: ")

    marks = []

    for i in range(3):
        mark = int(input(f"Enter mark for subject {i+1}: "))

        if mark < 0 or mark > 100:
            raise ValueError("Marks should be between 0 and 100")

        marks.append(mark)

    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\n----- Result -----")
    print("Student:", name)
    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Grade:", grade)

    save_result(name, marks, average, grade)

except ValueError as error:
    print("Error:", error)

except Exception as error:
    print("Unexpected error:", error)