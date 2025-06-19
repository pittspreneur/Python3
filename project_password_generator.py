# This script generates a random password using Python's string and random libraries.
# It selects printable characters from a specified range to construct a password of user-defined length.

import string, random#.......................allows function to print a random string 

def generatePassword(num):#..................fcn that creates the main payload
    password = ''#...........................declares the password as an empty string
    for n in range(num):#....................sets the scope for the payload
        x = random.randint(10,32)#...........number of charecters in code
        password += string.printable[x]#.....adds random charecters to compile into password

    return password#.........................brings back the payload

print(generatePassword(16))#.................prints the actual payload
