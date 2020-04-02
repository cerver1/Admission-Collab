#Module 1

def validateGPA():  
    user_gpa = input("Please enter your GPA: ")
    valid_gpa = "2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4.0"
    valid_list = valid_gpa.split(',')

    if user_gpa in valid_list: 
        return (float(user_gpa) * 20)
       
    else:
        print("Please enter a valid GPA between 2.0 and 4.0")
        return validateGPA()


def validateSAT():

    user_sat = input("Please enter your SAT score: ")
    final = int(user_sat)

    if final in range(400,921):
        return(0)
    elif final in range(930,1001):
        return(6)
    elif final in range(1010, 1191):
        return(10)
    elif final in range(1200, 1351):
        return(11)
    elif final in range(1360, 1601):
        return(12)
    else: 
        print("Your SAT score wasn't between 400..1600: ")
        return validateSAT()


def validateHighSchoolQuality():

    user_Quality = input("Please enter your HighSchool Quality score: ")

    if user_Quality == "0":
        return(0)
    elif user_Quality == "1":
        return(2)
    elif user_Quality == "2":
        return(4)
    elif user_Quality == "3":
        return(6)
    elif user_Quality == "4":
        return(8)
    elif user_Quality == "5":
        return(10)
    else: 
        print("HSQ score wasn't between 1..5")
        return validateHighSchoolQuality()

def validateDifficultyOfCurriculum():

    user_curriculum = input("Please enter the difficulty of your curriculum: ")

    if user_curriculum == "-2":
        return(-4)
    elif user_curriculum == "-1":
        return(-2)
    elif user_curriculum == "0":
        return(0)
    elif user_curriculum == "1":
        return(2)
    else: 
        print("Please enter a valid DOC score between -2..1")
        return validateDifficultyOfCurriculum()


def studentStatus():

    GPA = validateGPA()
    SAT = validateSAT()
    Quality = validateHighSchoolQuality()
    Difficulty = validateDifficultyOfCurriculum()
    
    return(GPA + SAT + Quality + Difficulty)

GPA = validateGPA()
SAT = validateSAT()
Quality = validateHighSchoolQuality()
Difficulty = validateDifficultyOfCurriculum()
    
print(GPA + SAT + Quality + Difficulty)
