# Module 1
from Util import When


def validateGPA():
    user_gpa = input("Please enter your GPA: ")
    valid_gpa = "2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4.0"
    valid_list = valid_gpa.split(',')

    if user_gpa in valid_list:
        return float(user_gpa) * 20
    print("Please enter a valid GPA between 2.0 and 4.0")
    return validateGPA()  # Exception solved; return function instead of an explicit call.


def validEntry():
    user_sat = input("Please enter your SAT score: ")
    try:
        final = int(user_sat)
        return final
    except:
        print("Please enter an SAT score between 400..1600: ")
        return validEntry()


def validateSAT():
    score = validEntry()
    try:
        when = When({
            range(400, 921): 0,
            range(930, 1001): 6,
            range(1010, 1191): 10,
            range(1200, 1351): 11,
            range(1360, 1601): 12,
        })
        return when[score]

    except:
        print("Your SAT score wasn't between 400..1600: ")
        return validateSAT()


def validateHighSchoolQuality():
    user_quality = input("Please enter your HighSchool Quality score: ")

    try:
        when = {
            '0': 0,
            '1': 2,
            '2': 4,
            '3': 6,
            '4': 8,
            '5': 10,
        }
        return when[user_quality]
    except:
        print("HSQ score wasn't between 1..5")
        return validateHighSchoolQuality()


def validateDifficultyOfCurriculum():
    user_curriculum = input("Please enter the difficulty of your curriculum: ")

    try:
        when = {
            '-2': -4,
            '-1': -2,
            '0': 0,
            '1': 2,
        }
        return when[user_curriculum]
    except:
        print("Please enter a valid DOC score between -2..1")
        return validateDifficultyOfCurriculum()


def studentStatus():
    gpa = validateGPA()
    sat = validateSAT()
    quality = validateHighSchoolQuality()
    difficulty = validateDifficultyOfCurriculum()

    points = gpa + sat + quality + difficulty

    print(f"\n\nTotal points the student earned are, {points}.")
    print(f"\n\nHere is the split:\n\nGPA points: {gpa}\nSAT points: {sat}")
    print(f"HighSchool Quality points: {quality}\nCurriculum Difficulty points: {difficulty}.\n")
    return int(points)
