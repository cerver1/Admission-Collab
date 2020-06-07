# Module 2

global alumni_score, ls_score, misc_score, essay_point


def validateGeography(state):  # Validate Geography Function
    if state == "State Resident":
        return 10
    else:
        return 0


def validateEssayScore(essay_score):  # Validate Essay Score Function
    if essay_score == "Very Good":
        return 1
    elif essay_score == "Excellent":
        return 2
    elif essay_score == "Outstanding":
        return 3
    else:
        return 999  # Returning a random number as flag if wrong value is entered


def validateMiscVenture(misc_venture):
    twenty_point_list = ["Socioeconomic disadvantage", "Scholarship athlete", "Provost's discretion"]
    if misc_venture in twenty_point_list:
        return 20
    elif misc_venture == "Men in Nursing":
        return 5
    else:
        return 999


def validateLeadership(leadership):  # Validate Leadership Function
    if leadership == "National":
        return 5
    elif leadership == "State":
        return 1
    elif leadership == "Regional":
        return 2
    else:
        return 999  # Returning a random number as flag if wrong value is entered


def validateAlumni(alumni):  # Validate Alumni Function
    if alumni == "Legacy":
        return 4
    elif alumni == "Other":
        return 1
    else:
        return 999  # Returning a random number as flag if wrong value is entered


def module2score():
    global alumni_score, ls_score, misc_score, essay_point

    print("Module 2 of college admission starts here\n\n")

    state = input("If the student is state resident please enter otherwise enter the state:")
    geo_points = validateGeography(state)

    flag = True  # Flag variable to check if correct value is entered
    while flag:  # While loop until correct value is entered
        essay_score = input("Enter essay score: ")
        essay_point = validateEssayScore(essay_score)
        if essay_point == 999:
            flag = True
        else:
            flag = False

    flag = True
    while flag:
        misc_venture = input("Enter any Miscellaneous venture: ")
        misc_score = validateMiscVenture(misc_venture)
        if misc_score == 999:
            flag = True
        else:
            flag = False

    flag = True
    while flag:
        leadership = input("Enter leadership/service: ")
        ls_score = validateLeadership(leadership)
        if ls_score == 999:
            flag = True
        else:
            flag = False

    flag = True
    while flag:
        alumni = input("Enter Alumni status (Legacyor Other): ")
        alumni_score = validateAlumni(alumni)
        if alumni_score == 999:
            flag = True
        else:
            flag = False

    points = geo_points + essay_point + misc_score + ls_score + alumni_score

    print(f"\n\nTotal points the student earned are, {points}.")  # Printing total points
    print(f"\n\nHere is the split:\nGeography points: {geo_points}\nEssay Point: {essay_point}")
    print(f"Misc Venture points: {misc_score}\nLeadership points: {ls_score}\nAlumni Points: {alumni_score}")
    return points
