#Module 2

def validateGeography(state):           #Validate Geography Function
    if state == "State Resident":
        return 10
    else:
        return 0

def validateEssayScore(essayScore):     #Validate Essay Score Function
    if essayScore == "Very Good":
        return 1
    elif essayScore == "Excellent":
        return 2
    elif essayScore == "Outstanding":
        return 3
    else:
         return 999                     #Returning a random number as flag if wrong value is entered

def validateMiscVenture(miscVenture):
    twentyPointList = ["Socioeconomic disadvantage","Scholarship athlete","Provost's discretion"]
    if miscVenture in twentyPointList:
        return 20
    elif miscVenture=="Men in Nursing":
        return 5
    else:
        return 999


def validateLeadership(leadership):     #Validate Leadership Function
    if leadership == "National":
        return 5
    elif leadership == "State":
        return 1
    elif leadership == "Regional":
        return 2
    else:
         return 999                     #Returning a random number as flag if wrong value is entered


def validateAlumni(alumni):     #Validate Alumni Function
    if alumni == "Legacy":
        return 4
    elif alumni == "Other":
        return 1
    else:
         return 999                     #Returning a random number as flag if wrong value is entered


points=0
print("Module 2 of college admission starts here\n\n")


state=input("If the student is state resident please enter otherwise enter the state:")
geoPoints=validateGeography(state)


flag = True                                         #Flag variable to check if correct value is entered 
while flag:                                         #While loop until correct value is entered
    essayScore= input("Enter essay score: ")
    essayPoint= validateEssayScore(essayScore)
    if essayPoint==999:
        flag=True
    else:
        flag=False

flag=True
while flag:
    miscVenture = input("Enter any Miscellaneous venture: ")
    miscScore = validateMiscVenture(miscVenture)
    if miscScore==999:
        flag=True
    else:
        flag=False


flag=True
while flag:
    leadership = input("Enter leadership/service: ")
    lsScore = validateLeadership(leadership)
    if lsScore==999:
        flag=True
    else:
        flag=False

flag=True
while flag:
    alumni = input("Enter Alumni status (Legacyor Other): ")
    alumniScore = validateAlumni(alumni)
    if alumniScore==999:
        flag=True
    else:
        flag=False

points = geoPoints + essayPoint + miscScore + lsScore + alumniScore

print(f"\n\nTotal points the student earned are, {points}.")                                                        #Printing total points
print(f"\n\nHere is the split:\nGeography points: {geoPoints}\nEssay Point: {essayPoint}")                          #Printing seprate points
print(f"Misc Venture points: {miscScore}\nLeadership points: {lsScore}\nAlumni Points: {alumniScore}")