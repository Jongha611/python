# Raise Exception
# custom error(user defined error)
class GradeOutOfBoundError(Exception):
    def __init__(self, grade, message):
        self.grade = grade
        self.message = message
        # do something here


grade = int(input("Type your score from 0 to 100: "))

try:
    if grade < 0 or grade > 100:
        raise GradeOutOfBoundError(
            grade=grade,
            message="Grade should be between 0 to 100"
        )
except GradeOutOfBoundError as e:
    print(f"inserted grade: {e.grade}, {e.message}")