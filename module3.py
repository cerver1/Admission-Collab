from module1 import studentStatus
from module2 import module2score

totalPoints = studentStatus() + module2score()

if totalPoints > 100:

    print(f"\nThis Student has been admitted!\n")

else:

    print(f"\nUnfortunately this Student has been denied.\n")
    print(totalPoints)
