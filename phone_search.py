"""
Program: phone_search.py
Author: Jeffrey Cosgrove
Date: 2/14/2020

This program allows a user to search a database for the first and last name and
phone number of the entries listed in the phones.txt file. The program accepts a
user input, then converts that input into lower case so that the program can cross
reference the text file and print out any line that contains the input by <first_name>
<last_name>, <phone_number>. Finally the program checks to see wether or not the user
wishes to restart and run another search or quit the program entirely.

Input: The name or phone number that is to be searched, as well as wether or not to
restart the program.

Output: Any line in the text document that matches the user's search query in the format
of <first_name> <last_name>, <phone_number>.
"""

#global varible declaration
cont = True
one = 1
two = 2

#main program loop
while cont == True:
    cont = True
    temp = 0
    name = input("Enter a name you would like to search: ").lower()

#search text file for user input, if found print line, otherwise return nothing
    f = open("phones.txt", 'r')
    while True:
        line = f.readline()
        lineLow = line.lower()
        if name in lineLow:
            firstName, lastName, phoneNum = line.split()
            print("\nName:  {} {}\nPhone: {}".format(firstName, lastName, phoneNum))
        if line == "":
            break
    f.close()

#restart program loop
    while temp == 0:
        temp = int(input("\nRestart Program? Enter 1 to start again and 2 to quit: "))
        if temp == 1:
            cont = True
            break
        if temp == 2:
            cont = False
            break
        else:
            temp = 0
