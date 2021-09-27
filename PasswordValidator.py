#Thomas Johnson
#CITC 1301-L01
#Assignment 9
#11/24/2020

def validatePassword(password):
    upperCount = 0
    numCount = 0
    lowerCount = 0
    pwLength = 0
    validPassword = "true"

    pwLength = len(password)
    print(password)
    for i in range(len(password)):
        print(password[i])
        if password[i].isupper():
            upperCount += upperCount
        if password[i].islower():
            lowerCount += lowerCount
        if password[i].isalnum():
            numCount += numCount
    print(upperCount)
    print(lowerCount)
    print(numCount)
    if pwLength < 5:
        validPassword = 'false'
        print('Pasword must be at least 5 characters long')

    if upperCount < 1:
        validPassword = 'false'
        print('Pasword must contain an uppercase letter')
    if lowerCount < 1:
        validPassword = 'false'
        print('Pasword must contain a lowercase letter')
    if numCount < 1:
        validPassword = 'false'
        print('Pasword must contain a number')

    validatePassword = validPassword

username = input('User Name: ')
validPW = 'false'

while validPW == 'false':
    password = input('Password: ')
    validPW = validatePassword(password)
    print('')

    
    



    
