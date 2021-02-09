#Password generator program
from random import choice
from datetime import date
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Password Generator")

print('Hello, this is a program that will generate you a new password!\n')

def mainFunction():
    words = []
    file = open('words.txt', 'r')
    words = file.read().splitlines()

    numbers = []
    file = open('numbers.txt','r')
    numbers = file.read().splitlines()

    newPassword = []
    theDate = []

    start = input('Press enter to generate password\t')
    print('\n')
    
    #Pick a random first word
    wordA = choice(words)
    newPassword.append(wordA)
    words.remove(wordA)

    #Pick a random number in between words
    numberA = choice(numbers)
    newPassword.append(numberA)
    numbers.remove(numberA)

    #Pick a random second word
    wordB = choice(words)
    newPassword.append(wordB)
    words.remove(wordB)
    
    #Add date when the password was generated
    today = date.today()
    theDate.append(today)

    #Save the generated password to the file
    yourNewPassword = newPassword
    with open ('newpassword.txt','w') as filehandle:
        for listitem in yourNewPassword:
            filehandle.write('%s' % listitem)
        for listitem in theDate:
            filehandle.write('\t\t%s' % listitem)

    print("Done! Check the newpassword.txt file for the generated password!\n")

    #Ask user if they want to see the generated password in the shell
    seeHere = input('Would you like to see the password here? [y/Y]?:\t')
    print('\n')
    if len(seeHere) > 0 and seeHere.isalpha() and seeHere[0].lower() == 'y':
        print(''.join(newPassword))
        print('\n')
    stop = input('Press enter to exit\t')
    
if __name__ == '__main__':
    mainFunction()