# Grading Program
# A if >= 90, B if >= 80, C if >= 70, otherwise F

students = {
    "tom": "82",
    "jerry": "93",
    "joon": "99",
    "misha": "80",
    "amy": "74",
    "sarah": "59"
}

def grader(name) -> str:
    score = int(students[name])
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
        
    return print(grade)

grader(input("what's your name? "))