# Programmer: Matias
# Description: Valid Triangle Angles
#Ask from user's triangle's information
angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))
print(" ")

#Calculate the total of all angles
total = angle1 + angle2 + angle3

#Print if triangle is valid or not
if total == 180:
    print("Triangle Is Valid!")
  
else:
    print("Triangle Is Not Valid!")
