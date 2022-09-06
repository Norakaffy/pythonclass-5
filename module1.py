#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kafonya Nora
#
# Created:     12/07/2021
# Copyright:   (c) Kafonya Nora 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import os

names = []
scores = []


names.append(input ("Enter Student's Name:"))
scores.append (int(input ("Enter Student's Scores: ")))

names.append(input ("Enter Student's Name:"))
scores.append (int(input ("Enter Student's Scores: ")))


names.append(input ("Enter Student's Name:"))
scores.append (int(input ("Enter Student's Scores: ")))

names.append(input ("Enter Student's Name:"))
scores.append (int(input ("Enter Student's Scores: ")))

names.append(input ("Enter Student's Name:"))
scores.append (int(input ("Enter Student's Scores: ")))

os.system("cls")

#print(names, scores)



print ("=" * 20)
print("NAMES\t  SCORES")
print (f"{names[0]}\t\t {scores[0]}")
print (f"{names[1]}\t\t {scores[1]}")
print (f"{names[2]}\t\t {scores[2]}")
print (f"{names[3]}\t\t {scores[3]}")
print (f"{names[4]}\t\t {scores[4]}")

#omotayo method
print (f"Highest Score is: {max(scores)}")
print (f"Highest Score is: {min(scores)}")


#ENE'S METHOD

scores.sort
print(f"Highest Scores is: {scores[4]}")
print(f"Lowest Score is: { scores[0]} ")

sum = scores[0] + scores[1] + scores[2] + scores[3] + scores[4];

avg = sum/len (scores)

print (f" the average score is {avg}")





