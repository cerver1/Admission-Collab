from module1 import studentStatus
from module2 import module2score

#missing process: combining the points from module 1 and module 2 
totalPoints = studentStatus() + module2score()
if totalPoints> 100 :
    
    print(f"\nThis Student has been admitted!\n")

else:

    print(f"\nUnfortunately this Student has been denied due to scores falling below requirements.\n")
    print(totalPoints)