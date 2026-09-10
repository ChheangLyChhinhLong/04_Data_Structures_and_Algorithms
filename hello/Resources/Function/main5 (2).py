def get_grade(score):
    if score >= 95:
        return "Excellence"
    elif score >= 85:
        return "Very good"
    elif score >= 75:
        return "Good"
    elif score >= 65:
        return "Fair"
    elif score >= 60:
        return "Passed"
    else:
        return "Failed"

student_score = float(input("Enter student score: "))

if 0 <= student_score <= 100:
    grade = get_grade(student_score)
    print(f"Score: {student_score} -> Grade: {grade}")
else:
    print("Invalid score! Please enter a score between 0 and 100.")