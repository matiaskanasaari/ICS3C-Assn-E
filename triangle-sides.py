# Programmer: Matias
# Description: Kanasaari

#Ask the lenghts of the sides
side1 = float(input("Enter a lenght of the first short side: "))
side2 = float(input("Enter a lenght of the second short side: "))           
side3 = float(input("Enter a lenght of the long side: "))
print(" ")

#Calculate the total of side2 and side2
total = side1 + side2

#Print if the Triangle is valid or not
if total > side3:
              print("Triangle Is Valid!")
else:
     print("Triangle Is Not Valid!")