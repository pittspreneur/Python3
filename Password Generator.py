'''Password Generator'''

import string, random#.......................allows function to printa random string 

def generatePassword(num):#..................fcn that creates the main payload
    password = ''#...........................declares the password as a password


    
    for n in range(num):#....................sets the scope for the payload
        x = random.randint(10,32)#...........number of charecters in code
        password += string.printable[x]#.....adds random charecters to compile into password

    return password#.........................brings back the payload

print(generatePassword(16))#.................prints the actual payload
