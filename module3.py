#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kafonya Nora
#
# Created:     13/07/2021
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

names.append(input("Enter Student Name:"))
scores.append(int(input("Enter Student's score: ")))

names.append(input("Enter Student Name:"))
scores.append(int(input("Enter Student's score: ")))

names.append(input("Enter Student Name:"))
scores.append(int(input("Enter Student's score: ")))

names.append(input("Enter Student Name:"))
scores.append(int(input("Enter Student's score: ")))


names.append(input("Enter Student Name:"))
scores.append(int(input("Enter Student's score: ")))

os.system("cls")

#print(names, scores)


print("=" * 20)

print ("NAMES\t  SCORES")
print (f"{names[0]}\t\t {scores[0]}")
print (f"{names[1]}\t\t {scores[1]}")
print (f"{names[2]}\t\t {scores[2]}")
print (f"{names[3]}\t\t {scores[3]}")
print (f"{names[4]}\t\t {scores[4]}")

