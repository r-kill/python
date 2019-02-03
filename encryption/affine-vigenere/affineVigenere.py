global TEXT

charSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*']

def main():
    print('\n\nAssignment 2 - Affine-Vigenere Cipher')
    
    #ask user if they want to ENCRYPT or DECRYPT
    exitProgramFlag = False
    while exitProgramFlag == False:
        exitMenuFlag = False
        while exitMenuFlag == False:
            print('\n\nEnter EXIT to exit this program.')
            print('Enter an E to encrypt your plaintext string.')
            print('Enter a D to decrypt your ciphertext string.')
            mode = input('\nEXIT, (E)ncrypt or (D)ecrypt: ').lower()
            
            #assume bad input until input check function returns true
            #while input is bad, ask user for new input until it's good
            correctInput = False
            while correctInput == False:
                #check for correct input
                while (mode != 'e') and (mode != 'd') and (mode != 'exit'):
                    print('\n\nPlease only enter an E, a D or EXIT.')
                    mode = input('\nEXIT, (E)ncrypt or (D)ecrypt: ').lower()
                    
               #show user charSet to give them a list of options, only if they don't want to exit
                if mode != 'exit':
                    #these flags used to separate letters from numbers and nums from symbols
                    isnumericFlag = True
                    oneTimeFlag = True
                    print('\n\nYour input can contain any of these characters:')
                    print('    ', end='')
                    for num in range(len(charSet)):
                        #create separation when letters switch to nums + when nums switch to symbols
                        if ((charSet[num].isnumeric()) and (isnumericFlag == True)):
                            print('\n    ', end='')
                            isnumericFlag = False
                        #create separation between numbers and symbols only one time
                        #char in charSet can't be numeric, signifies end of numbers in charSet
                        #isnumericFlag must be False, shows that nums were separated from letters
                        #oneTimeFlag will be set to False in elif so it won't add new line for each num
                        elif ((charSet[num].isnumeric()) == False) and (isnumericFlag == False) and (oneTimeFlag == True):
                            print('\n    ', end='')
                            oneTimeFlag = False
    
                        #print character
                        print(charSet[num], end=' ')
                    
                    #print an extra blank line for readability
                    print()
                
                #perform different actions if user chose to encrypt or decrypt
                if mode == 'e':
                    print('\nYou\'ve chosen to ENCRYPT your palintext string.')
                    PT = input('Enter the plaintext string you\'d like to ENCRYPT: ').lower()
                    
                    #set global variable TEXT to user input so only one variable needs to be manipulated
                    TEXT = PT
                    
                    #set exitMenuFlag and correctInput to true in order to break out of the while loops
                    exitMenuFlag = True
                    correctInput = True
                elif mode == 'd':
                    print('\nYou\'ve chosen to DECRYPT your cyphertext string.')
                    CT = input('Enter the cyphertext string you\'d like to DECRYPT: ').lower()
                    
                    #set global variable TEXT to user input so only one variable needs to be manipulated
                    TEXT = CT
                    
                    #set exitMenuFlag and correctInput to true in order to break out of the while loops
                    exitMenuFlag = True
                    correctInput = True
                elif mode == 'exit':
                    #verify users choice + exit if they choose to, error check input along the way
                    flag = input('\nAre you sure you want to exit this program? (Y)es or (N)o: ').lower()
                    
                    #verify input is correct
                    while (flag != 'n') and (flag != 'y'):
                        print('Please only enter a Y for Yes or an N for No.')
                        flag = input('\nAre you sure you want to exit the program? (Y)es or (N)o: ').lower()
                    
                    #exit if user inputs Y and go to main menu if user inputs N
                    if flag == 'y':
                        print('\nThank you for using this encryption/decryption program.')
                        return
                    elif flag == 'n':
                        print('\nGoing back to the main menu...')
                        
                        #change flags to break out of while loops
                        #don't need to change these in above if because of the return statemtent
                        exitMenuFlag = False
                        correctInput = True
                    continue
                
                #check input for errors
                while not errorCheck(TEXT):
                    #if program enters this block, TEXT is empty str or has chars outside of charSet
                    correctInput = False
                    break
        
        #get KEY from user, ask for new KEY until user inputs a KEY that satisfies conditions
        correctKey = False
        print('\n\nA KEY string is used to encrypt/decrypt the input string you just entered:')
        print(' -If the KEY is longer than the input string,')
        print('    then the excess characters in the KEY won\'t be used.')
        print(' -The KEY must NOT be the same string as the input string.')
        print(' -The KEY must only use characters from those shown above.')
        print(' -The KEY must not have any repeated characters in it.')
        print(' -Avoid keys like "STONES" and favor keys like "DISPLAY".')
        K = input('\nPlease input a KEY: ').lower()
        
        #assume input is erroneous until fxns prove otherwise
        while correctKey == False:
            #error check KEY
            K = checkDuplicates(K)
            
            #checks if KEY is same string as input PT/CT, make sure KEY isn't empty string
            #get new KEY from user until it has no duplicates and isn't same string as PT/CT
            if (K == TEXT) and (K != ''):
                while (K == TEXT) and (K != ''):
                    print('\nYou entered a KEY that\'s identical to the PLAINTEXT or CIPHERTEXT.')
                    print('The KEY must not be the same string as PLAINTEXT or CIPHERTEXT.')
                    K = input('\nPlease enter another KEY: ').lower()
                
                #check new KEY input for duplicates and for equivalence to PT/CT
                K = checkDuplicates(K)
                correctKey = False
            elif (K != TEXT) and (K != ''):
                correctKey = True
            
            #check input for errors
            while not errorCheck(K):
                #if program enters this block, TEXT is empty str or has chars outside of charSet
                correctKey = False
                K = input('\nPlease enter another KEY: ').lower()
                break
        
        #find numbers that are relatively prime to len(charSet) and populate a list with those values
        #creating betaSet list and appending relative primes to it
        betaSet = []
        for num in range(1, len(charSet)+1):
            beta = num
            var = len(charSet)
            
            #get gcd(len(charSet), BETA)
            while var != beta:
                if beta > var:
                    beta -= var
                else:
                    var -= beta
            if beta == 1:
                betaSet.append(num)
        
        #get beta value from user + check if it's within the set of possible beta values
        print('\n\nNext you will need to enter a BETA VALUE for the algorithm.')
        print(' -The BETA VALUE needs to be relatively prime to', str(len(charSet)) + 
             '. It\'s just a multiplier.')
        print(' -You should choose one of these numbers for your BETA:', end='\n     ')
        #print values in beta set for user reference and get BETA input
        B = ''
        B =  getBeta(B, betaSet)
        
        #error checking BETA
        if ((B.isnumeric()) == False) or ((B in betaSet) == False):
            #if BETA isn't numeric (Pythons definition of numeric) have user input another BETA
            #if BETA isn't in betaSet, have user input another BETA until it is in betaSet
            while ((B.isnumeric()) == False) or ((B in str(betaSet)) == False):
                print('\n\nYou must enter a BETA VALUE that is relatively prime to 46.')
                print(' -Please choose one of these numbers:', end='\n     ')
                B = getBeta(B, betaSet)
            
        
        #convert TEXT (which is PT or CT) chars into decimal values according to charSet
        decText = []
        for char in TEXT:
            decText.append(charSet.index(char))
        
        #convert chars in K to their individual charSet decimal values
        decKey = []
        for char in K:
            #if KEY longer than TEXT, don't convert excess KEY chars to decimals
            if len(decKey) < len(decText):
                decKey.append(charSet.index(char))
            else:
                break
    
        #if K is shorter than TEXT, then repeat chars in K until len(K) == len(TEXT)
        #this works AFTER decKey and decText are filled with decimal values
        if len(decKey) < len(decText):
            index = 0
            while len(decKey) < len(decText):
                decKey.append(decKey[index])
                index += 1
        
        #ready to do multiplication and output based on mode (encrypt/decrypt)
        if mode == 'e':
            #if in encrypt mode, get the ciphertext by first encrypting each char in PT
            cipherTextChars = []        
            for char in decText:
                cipherChar = (decKey[decText.index(char)] + (int(B) * int(char))) % len(charSet)
                cipherTextChars.append(cipherChar)
            
            #next convert chars in cipherTextChars list to charSet values
            cipherText = convertToCharSet(cipherTextChars)
            
            #output encryption
            output(K, B, TEXT, cipherText)
        elif mode == 'd':
            #get inverse of BETA for decryption
            betaInverse = findInverse(B)
            
            #if in decrypt mode, get the plaintext by first decrypting each char in CT
            plainTextChars = []
            for char in decText:
                plainChar = ((decText[decText.index(char)] - decKey[decText.index(char)]) * (int(betaInverse) % len(charSet))) % len(charSet)
                plainTextChars.append(plainChar)
                    
            #next convert chars in plainTextChars list to charSet values
            plainText = convertToCharSet(plainTextChars)
            
            #output decryption
            output(K, betaInverse, TEXT, plainText)
        
        #ask user if they would like to restart the program
        userExit = input('\nWould you like to encrypt/decrypt another string? (Y)es or (N)o: ').lower()
        
        #make sure user only inputs Y or N
        while (userExit != 'y') and (userExit != 'n'):
            print('\nPlease only enter "Y" for yes and "N" for no.')
            userExit = input('Would you like to encrypt/decrypt another string? (Y)es or (N)o: ').lower()
        
        #return to main menu if user inputs Y and exit if inputs N
        if userExit == 'y':
            exitProgramFlag = False
        elif userExit == 'n':
            exitProgramFlag = True
            print('\nThank you for using this encryption/decryption program.')

#function for checking if input is in charSet
def errorCheck(usrInput):
    #check input for empty string
    if (len(str(usrInput)) == 0) or (str(usrInput) == ' '):
        print('\nIt appears as though you\'ve entered an empty string.')
        print('Please enter an appropriate value.')
        return False
    
    #check TEXT/KEY for any characters that are not in charSet
    for char in usrInput:
        if char not in charSet:
            print('\nIt looks like you\'ve used a character that is not acceptable.')
            print(' -Please only use letters A - Z (uppercase and lowercase will be treated the same).')
            print(' -Please only use the numbers 0 - 9 (10 will be counted as two individual numbers).')
            print(' -Please only use these special characters: ! " # $ % & \' ( ) * (exclude spaces).')
            return False
                
    #return True to main to signify no errors in input
    return True

#function to concatenate a list of characters into a string after 
#converting the individual chars to their correcponding charSet values
def convertToCharSet(usrInput):
    #next concat the list of plaintext chars into one string
    for index in range(len(usrInput)):
        #change the list of decimal values (cipherTextChars) to their charSet values
        usrInput[index] = charSet[usrInput[index]]
            
    #cipherTextChars is a list of characters, concat them into one string and return it
    newText = ''
    newText = newText.join(usrInput)
    return newText

#function to handle Euclidean GCD algorithm in order to find the inverse of a value
#in this case the value is BETA so pass B to fxn
def findInverse(B):
    #get inverse of BETA for decryption
    #finds inverse of findInverse given the equation findInverse mod modValue
    #modValue is usually the length of the charSet
    findInverse = B
    modValue = len(charSet)
    
    #ax + by = gcb(a,b)
    a = findInverse
    b = modValue
    
    #x and y are used to start the X-side Euclidean GCD algorithm table as x0 = 1 and x1 = 0
    x = 1               #x0 = 1
    y = 0               #x1 = 0
    
    #this is the code for the Euclidean GCD algorithm
    while(b != 0):
        #find a num such that num * findInverse <= modValue (e.g. 6*7=42 <= 46 and 7*7=49 > 46)
        quotient = int(a) // int(b)
        #get the remainder of ((num * findInverse) - modValue)
        #e.g. ((7 * 6) - 46) = 4
        remainder = int(a) - (int(quotient) * int(b))
        #this equation is equivalent to x2 = -q1 * x1 + x0 from Euclideam GCD algorithm
        euclideanResult = int(x) - (int(quotient) * int(y))
        #set x equal to y value to increment x0 to x1, x1 to x2, x2 to x3,... [x1 == x subscript 1]
        x = y
        #set x0 to x1 by setting x to y, then set x1 to x2 by setting y to euclideanResult
        #set y equal to euclideanResult (or x2) value to increment x1 to x2, x2 to x3, x3 to x4,...
        y = euclideanResult
        #set a to b so b will shift to the correct position in the next iteration of the equation
        a = b
        #now set b to remainder so the remainder is in the correct position in the next iteration
        b = remainder
        
    #now x is the inverse of findInverse so return that value
    return x

#function to check a string for duplicate characters, asks for new input if duplicate found
def checkDuplicates(K):
    #error check KEY
    dupeFlag = True      #assume KEY has duplicates when input so set this flag to True
    count = 0
    while (count < len(K)) and (dupeFlag == True) and (K != ''):
        for char in K:
            if K.count(char) > 1:
                while K.count(char) > 1:
                    #while a char in KEY is counted >1 time, ask user for new KEY
                    #a KEY w/ no duplicates should not have more than 1 of any char in KEY
                    print('\nIt appears that you\'ve entered a KEY that contains duplicate characters.')
                    K = input('Please input another KEY that does NOT contain duplicate characters: ').lower()
                    #checks new KEY for duplicates before returning anything
                    dupeFlag = True
                    count = 0
                    break
            else:
                #if a char in KEY is counted <=1 time, then it's not repeated elsewhere in KEY
                count += 1
                dupeFlag = False
            #if duplicates detected, break out of for loop + check new KEY
            if dupeFlag == True:
                break
    #return KEY that has no duplicates
    return K

#get BETA input from user, also prints values in betaSet neatly
def getBeta(B, betaSet):
    #print values in beta set for user reference
    for item in betaSet:
        #check index of each value in betaSet to verify it exists within betaSet
        if betaSet.index(item) != (len(betaSet) - 1):
            if (betaSet.index(item) % 10 == 0) and (betaSet.index(item) != 0):
                #nested if separates the line of numbers for user readability
                print('\n     ', end='')
            print(str(item).zfill(2), end=', ')
        elif betaSet.index(item) == (len(betaSet) - 1):
            #the elif does not print a comma after last item in betaSet
            print(str(item).zfill(2)) 
    B = input('\nPlease enter a BETA VALUE: ').lower()
    
    #return BETA with all leading zeros stripped if it contains more than one char
    #prevents an input of 0 from returning an empty string
    if len(B) > 1:
        return B.lstrip('0')
    else:
        return B

#prints output for encryption and decryption
def output(KEY, BETA, PT, CT):
    #begin output for encryption
    print('\n\nHere are the variable details for this session:')
    print('\tNominal Values \t\t\tOrdinal Values')
    print('\n    KEY\tBETA  Input  PT/CT      KEY\tBETA  Input   PT/CT')
    print('  --------------------------  -------------------------------')
    item = 0
    while item in range(len(CT)):
        #print a new line after ORDINAL CT is printed so next KEY can be on a new line
        if (item != 0) and (item % 8 == 0):
            print()
        
        #print both nominal and ordinal value tables
        print('     ' + KEY[(item % len(KEY))] + '\t ' + str(BETA).zfill(2) + '\t' + 
             PT[item] + '      ' + CT[item] + 
             '        ' + str(charSet.index(KEY[(item % len(KEY))])).zfill(2) + 
             '\t ' + str(BETA).zfill(2) + 
             '\t' + str(charSet.index(PT[item])).zfill(2) + 
             '     ' + str(charSet.index(CT[item])).zfill(2))
        
        item += 1
    
    #if the KEY is longer than the TEXT and not all of the KEY is used, print unused values
    #only needed for KEY because len(PT) == len(CT) and BETA is one number that's a multiplier.
    if (len(KEY) > len(str(BETA))) and (len(KEY) > len(PT)) and (len(KEY) > len(CT)):
        while item in range(len(KEY)):
            #print a new line after ORDINAL CT is printed so next KEY can be on a new line
            if (item != 0) and (item % 8 == 0):
                print()
            
            #print excess characters of KEY that weren't used in the algorithm
            #this happend when KEY is longer than TEXT
            #prints appropriate values for both tables
            print('     ' + KEY[(item % len(KEY))] + '\t ' + str(BETA).zfill(2) + 
            '\t-      -        ' + str(charSet.index(KEY[(item % len(KEY))])).zfill(2) + 
            '\t ' + str(BETA).zfill(2) + '\t--     --')
           
            item += 1
    #print one last blank line for readability
    print()

main()
