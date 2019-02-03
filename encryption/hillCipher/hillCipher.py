'''
Hill Cipher Program
Rowan Kill
'''

global TEXT

charSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*']

def main():
    print('\n\nAssignment 3 - Hill Cipher with a 2x2 or 3x3 Matrix')
    
    #ask user if they want to ENCRYPT or DECRYPT
    exitProgramFlag = False
    while exitProgramFlag == False:
        exitMenuFlag = False
        while exitMenuFlag == False:
            print('\n\nEnter EXIT to exit this program.')
            print('Enter an E to encrypt your plaintext string.')
            print('Enter a D to decrypt your cyphertext string.')
            mode = input('\nEXIT, (E)ncrypt or (D)ecrypt: ').lower()
            
            #assume bad input until input check function returns true
            #while input is bad, ask user for new input until it's good
            correctInput = False
            while correctInput == False:
                #check for correct input
                while (mode != 'e') and (mode != 'd') and (mode != 'exit'):
                    print('\n\nPlease only enter an E, a D or EXIT.')
                    mode = input('\nEXIT, (E)ncrypt or (D)ecrypt: ').lower()
                    
                #show user charSet + give them a list of rules, only if they don't want to exit
                if mode != 'exit':
                    #warn user that input depends on matrix size and should be certain lengths
                    print('\n\nRULES FOR INPUT:')
                    print(' -This program ONLY handles 2x2 and 3x3 matrices.')
                    print(' -Input should be able to fit into ONE ROW of the desired matrix.')
                    print(' -Matrix size is chosen by user after entering plaintext/ciphertext.')
                    print(' -2x2 matrix (two rows and two columns):')
                    print('   *Encrypts/decrypts FOUR characters max, TWO characters min')
                    print('   *Any excess characters after the FOURTH character are ignored')
                    print('   *Input values must be between 1 and 4 characters, inclusive')
                    print('   *Input values with less than TWO characters will be padded')
                    print('     with asterisks as needed.')
                    print(' -3x3 matrix (three rows and three columns):')
                    print('   *Encrypts/decrypts NINE characters max, THREE characters min')
                    print('   *Any excess characters after the NINTH character are ignored')
                    print('   *Input values must be between 1 and 9 characters, inclusive')
                    print('   *Input values with less than THREE characters will be padded')
                    print('     with asterisks as needed.')
                    input('Press ENTER after reading these rules carefully.')
                    
                    #these flags used to separate letters from numbers and nums from symbols
                    isnumericFlag = True
                    oneTimeFlag = True
                    print('\nALPHABET or CHARACTER SET:')
                    print(' -Your input can contain any of the characters in this set:')
                    print('    ', end='')
                    for num in range(len(charSet)):
                        #create separation when letters switch to nums + when nums switch to symbols
                        if ((charSet[num].isnumeric()) and (isnumericFlag == True)):
                            print('\n    ', end='')
                            isnumericFlag = False
                        #create separation between numbers and symbols only one time
                        #char in charSet can't be numeric, signifies end of numbers in charSet
                        #isnumericFlag must be False, shows that nums were separated from letters
                        #oneTimeFlag set to False in elif so it won't add new line for each num
                        elif (((charSet[num].isnumeric()) == False) and (isnumericFlag == False) 
                                and (oneTimeFlag == True)):
                            print('\n    ', end='')
                            oneTimeFlag = False
    
                        #print character
                        print(charSet[num], end=' ')
                    #print an extra blank line for readability
                    print()
                
                #perform different actions if user chose to encrypt or decrypt
                if mode == 'e':
                    print('\nYou\'ve chosen to ENCRYPT your plaintext string.')
                    PT = input('Enter the plaintext string you\'d like to ENCRYPT: ').lower()
                    
                    #set global variable TEXT to user input so only one variable is manipulated
                    TEXT = PT
                    
                    #set exitMenuFlag and correctInput to true to break out of while loops
                    exitMenuFlag = True
                    correctInput = True
                elif mode == 'd':
                    print('\nYou\'ve chosen to DECRYPT your ciphertext string.')
                    CT = input('Enter the ciphertext string you\'d like to DECRYPT: ').lower()
                    
                    #set global variable TEXT to user input so only one variable is manipulated
                    TEXT = CT
                    
                    #set exitMenuFlag and correctInput to true to break out of while loops
                    exitMenuFlag = True
                    correctInput = True
                elif mode == 'exit':
                    #verify users choice + exit if they choose to, error check input along the way
                    flag = input('\nAre you sure you want to ' +
                                 'exit this program? (Y)es or (N)o: ').lower()
                    
                    #verify input is correct
                    while (flag != 'n') and (flag != 'y'):
                        print('\nPlease only enter a Y for Yes or an N for No.')
                        flag = input('Are you sure you want to ' +
                                     'exit the program? (Y)es or (N)o: ').lower()
                    
                    #exit if user inputs Y and go to main menu if user inputs N
                    if flag == 'y':
                        print('\nThank you for using this encryption/decryption program.')
                        return
                    elif flag == 'n':
                        print('\nGoing back to the main menu...')
                        
                        #change flags to break out of while loops
                        #don't need to change these in above if because of the return statement
                        exitMenuFlag = False
                        correctInput = True
                    continue
                
                #this error check must come before error check for matrixCols
                #check input for errors
                while not errorCheck(TEXT):
                    #if program enters this block, TEXT is empty str or has chars outside of charSet
                    correctInput = False
                    break
        
        #assume that the number of columns input is not an acceptable value
        #loop and get new value until an acceptable one is input
        badMatrixDims = True
        while badMatrixDims == True:
            #if user inputs an acceptable TEXT value, then ask how many columns in matrices
            print('\n\nThe string must be split into sections or blocks.')
            print(' -For example, "GOOD" can be sectioned into blocks GO and OD.')
            print(' -This example shows a 2x2 matrix, having 2 rows and 2 columns.')
            print(' -There are 2 characters per block and 4 characters total.')
            print(' -A 3x3 matrix has 3 rows and 3 columns, containing 3 characters')
            print('    per block and 9 characters total.')
            print(' -This program only handles 2x2 and 3x3 matrices.')
            matrixCols = input('\nEnter the number of characters per block (2 or 3): ').lower()
            
            #error check matrixCols
            while (matrixCols != str(2)) and (matrixCols != str(3)):
                print('\nThe number of characters per block ' +
                      'must be either 2 or 3 for this program.')
                matrixCols = input('Enter a new value for the number ' +
                                    'of characters per block: ').lower()
                badMatrixDims = False
            while errorCheck(matrixCols):
                #if program enters this block, matrixCols is NOT an empty str
                badMatrixDims = False
                break
            
            #dynamically add nested lists to the userMatrix list based on matrixCols
            #each nested list contains matrixCols values before a new nested list starts
            #populate the nested lists with decimal values for chars from TEXT
            #if num chars in TEXT is less then matrixCols, pad with *
            if badMatrixDims == False:
                userMatrix = [[]]
                count = 0
                rowNum = 0
                for char in TEXT:
                    if ((len(userMatrix) < int(matrixCols)) or 
                        (len(userMatrix[rowNum]) < int(matrixCols))):
                        #create new nested list + increment rowNum to start appending char values
                        if (count % int(matrixCols) == 0) and (count > 0):
                            userMatrix.append([])
                            rowNum += 1
                        #append decimal value for char in TEXT to nested list
                        userMatrix[rowNum].append(charSet.index(char))
                        count += 1
                #if input shorter than size of a row of matrix, pad userMatrix with *s as needed
                printOnceFlag = ''
                while ((len(userMatrix[rowNum]) < int(matrixCols)) and 
                        (len(userMatrix) <= int(matrixCols))):
                    if printOnceFlag == '':
                        print('\nWARNING!!! YOUR INPUT HAS BEEN ALTERED!!!')
                        print(' -The string was too short to fill its matrix properly.')
                        print(' -The string was padded with asterisks as necessary.')
                        printOnceFlag = '-1'
                    #create new nested list + increment rowNum to start appending char values
                    if (count % int(matrixCols) == 0) and (count > 0):
                        userMatrix.append([])
                        rowNum += 1
                    #append decimal value for char in TEXT to nested list
                    userMatrix[rowNum].append(charSet.index('*'))
                    count += 1
                
                #if input is longer than size of matrix, tell user which chars weren't used
                if len(TEXT) > int(matrixCols)**2:
                    print('\nWARNING!!! YOUR INPUT HAS BEEN ALTERED!!!')
                    print(' -The string was too long to fit in its matrix properly.')
                    print(' -The excess characters in the string were ignored.')
                    printOnceFlag = '-1'
                
                #if input needs to be altered, show it to user
                if printOnceFlag != '':
                    print(' -The ALTERED input string is: ', end='')
                    for value in userMatrix:
                        for nestValue in value:
                            print(charSet[nestValue], end='')
                    printOnceFlag = input('\nPress ENTER to continue...')
    
                    #TEXT should be set to new value of user input if it was changed
                    TEXT = ''
                    for block in userMatrix:
                        for item in block:
                            TEXT += TEXT.join(charSet[item])
        
        #get KEY from user, ask for new KEY until user inputs a KEY that satisfies conditions
        badKey = True
        while badKey == True:
            correctKey = False      #used for error checking
            print('\n\nEnter a KEY string that\'s used to ' +
                 'transform the input string entered earlier.')
    
            if matrixCols == str(2):
                print(' -The KEY must have exactly 4 characters to fill the 2x2 matrix.')
            elif matrixCols == str(3):
                print(' -The KEY must have exactly 9 characters to fill the 3x3 matrix.')
            
            print(' -The KEY must NOT be the same string as the input string.')
            print(' -The KEY must only use characters from ' +
                  'those shown in the alphabet above.')
            print(' -Short KEYs will be padded with letters ' +
                  'of the alphabet in order (a, b, c,...)')
            print(' -Long KEYs will contain excess characters, these will be ignored.')
            K = input('\nPlease input a KEY: ').lower()
            
            #assume input is erroneous until fxns prove otherwise
            while correctKey == False:
                #check input for errors
                while not errorCheck(K):
                    #if program enters this block, KEY is empty str or has chars outside of charSet
                    correctKey = False
                    K = input('\nPlease enter another KEY: ').lower()
                    K = K[:int(matrixCols)**2]
                
                #strip excess letters off of KEY
                K = K[:int(matrixCols)**2]
                
                #checks if KEY is same string as input PT/CT, make sure KEY isn't empty string
                #get new KEY from user until it isn't same string as PT/CT
                if (K == TEXT) and (K != ''):
                    while (K == TEXT) and (K != ''):
                        print('\nYou entered a KEY that\'s identical ' +
                             'to the PLAINTEXT or CIPHERTEXT.')
                        print(' -The KEY must not be the same string ' +
                              'as PLAINTEXT or CIPHERTEXT.')
                        K = input('\nPlease enter another KEY: ').lower()
                        K = K[:int(matrixCols)**2]
                    
                    #check new KEY input for equivalence to PT/CT
                    correctKey = False
                elif (K != TEXT) and (K != ''):
                    break
            
            #convert chars in K to their individual charSet decimal values
            #make sure KEY is long enough to fill matrix
            #if it isn't long enough, tell user what was added 
                #KEY + a, b, c, d,... until long enough
            #if it is too long, tell user what was ignored
            keyMatrix = [[]]
            charIndex = 0
            count = 0
            rowNum = 0
            onlyPrintOnce = 0
            errorFlag = False
            #user input can be shorter than key so compare rows of key to first row of TEXT
            while ((len(keyMatrix[rowNum]) != int(matrixCols)) or 
                    (len(keyMatrix) != int(matrixCols))):
                #only fill key matrix with chars in KEY (input by user) one time
                if count == 0:
                    for char in K:
                        #KEY needs to be either 2x2 or 3x3
                        #user input can be shorter than key so compare rows of key to first row of TEXT
                        if ((len(keyMatrix[rowNum]) != int(matrixCols)) or 
                            (len(keyMatrix) != int(matrixCols))):
                            #create new nested list and increment rowNum to start adding char values to it
                            if (count % int(matrixCols) == 0) and (count > 0):
                                keyMatrix.append([])
                                rowNum += 1
                            #append decimal value for char in TEXT to nested list
                            keyMatrix[rowNum].append(charSet.index(char))
                            count += 1
                        elif ((len(keyMatrix) == int(matrixCols)) and 
                                (count == int(matrixCols)**2)):
                            print('\nYou entered a KEY that\'s long ' +
                                    'enough to over-fill the KEY matrix.')
                            print(' -The excess characters needed will not be used.')
                            #print remaining characters in K
                            print(' -These are the characters that weren\'t used:', K[count:])
                            count += 1
                            #set errorFlag to true to change value of K variable
                            errorFlag = True
                else:
                    #now all chars in KEY are put into the key matrix
                    #create new nested list, increment rowNum to start adding charSet chars to it
                    if (count % int(matrixCols) == 0):
                        keyMatrix.append([])
                        rowNum += 1
                    #append decimal value for chars in charSet to nested list
                    #until nested list is as long as user matrix
                    keyMatrix[rowNum].append(charSet.index(charSet[charIndex]))
                    charIndex += 1
                    count += 1
                    
                    #tell user that input was changed and show alteration
                    if (onlyPrintOnce == 0) and (count == int(matrixCols)**2):
                        print('\nYou entered a KEY that\'s not long enough ' +
                                'to fill the KEY matrix.')
                        print(' -The remaining characters needed will ' +
                                'be taken from the alphabet')
                        print('  (or character set) shown above.')
                        print(' -The new KEY is: ', end='')
                        for block in keyMatrix:
                            for item in block:
                                print(charSet[item], end='')
                        print()
                        onlyPrintOnce = 1
                        #set errorFlag to true to change value of K variable
                        errorFlag = True
                
            #set KEY to its new value if it was altered
            if errorFlag == True:
                input('Press ENTER to continue...')
                K = K[:int(matrixCols)**2]
            
            #assume input is erroneous until fxns prove otherwise
            #check KEY for errors again after converting to key matrix
            #this loop is a backup error check
            while correctKey == False:
                #checks if KEY is same string as input PT/CT, make sure KEY isn't empty string
                #get new KEY from user until it isn't same string as PT/CT
                if (K == TEXT) and (K != ''):
                    while (K == TEXT) and (K != ''):
                        print('\nYou entered a KEY that\'s identical ' +
                             'to the PLAINTEXT or CIPHERTEXT.')
                        print(' -The KEY must not be the same string ' +
                              'as PLAINTEXT or CIPHERTEXT.')
                        K = input('\nPlease enter another KEY: ').lower()
                    
                    #check new KEY input for equivalence to PT/CT
                    correctKey = False
                elif (K != TEXT) and (K != ''):
                    correctKey = True
                
                #set KEY to its new value if it was altered
                if errorFlag == True:
                    K = K[:int(matrixCols)**2]
                
                #check input for errors
                while not errorCheck(K):
                    #if program enters this block, KEY is empty str or has chars outside of charSet
                    correctKey = False
                    K = input('\nPlease enter another KEY: ').lower()
                    K = K[:int(matrixCols)**2]
                    break
                        
            #get determinant, inverse key, and identity matrix
            #inverse key and ID matrix aren't directly used in encryption
            #but they still need to be found now to determine usability of key in general
            #warn user if key cannot be used for decryption        
            keyModifyOutput = []
            keyModifyOutput = keyModify(keyMatrix, matrixCols)
            determinant = keyModifyOutput[0]
            inverseKey = keyModifyOutput[1]
            identity = keyModifyOutput[2]
            
            #check to make sure identity matrix only contains ones and zeros
            badID = True
            for row in identity:
                #if identity matrix is correct, then any row contains 2 to 3 total ones and zeros
                #row will contain 3 total ones + zeros for 3x3 and 2 total ones + zeros for 2x2
                if (((row.count(0) + row.count(1)) == int(matrixCols)) 
                    and (row.count(1) > 0) and (row.count(0) > 0)):
                    badID = False
                    break
                else:
                    #else ID matrix is incorrect and badID flag remains True
                    break
            
            #determine if KEY is good or bad based on GCD and identity matrix
            if (findInverse(determinant, len(charSet), True) != 1) and (badID == True):
                print('\nWARNING!! There may be an issue with the KEY!')
                print(' -This KEY will not be able to DECRYPT the input string.')
                print(' -The Hill Cipher requires a different ' +
                        'KEY in order to modify the input.')
                print(' -Enter (Y)es to change the KEY or enter ' +
                        '(N)o to prevent decryption.')
                badKey = input('\nWould you like to change the KEY? ' +
                                '(Y)es or (N)o: ').lower()
                
                #verify user input for continuing with bad KEY or not
                while (badKey != 'n') and (badKey != 'y'):
                    print('\nPlease only enter a Y for Yes or an N for No.')
                    badKey = input('Would you like to change the KEY? ' +
                                    '(Y)es or (N)o: ').lower()
                
                #enter a new KEY or continue with bad KEY
                if badKey == 'y':
                    print('\nEnter a new KEY...')
                    badKey = True
                    continue
                elif badKey == 'n':
                    print('\nYou\'ve chosen to continue with a BAD KEY.')
                    input('Press ENTER to continue...')
                    break
            else:
                badKey = False

        #ready to do multiplication and output based on mode (encrypt/decrypt)
        if mode == 'e':
            #if in encrypt mode, get the ciphertext by first encrypting each char in PT
            #multiply each row in PT by each column in KEY
            cipherText = [[]]
            total = 0
            for row in range(int(matrixCols)):
                if len(userMatrix) > row:
                    for userCols in range(int(matrixCols)):
                        for col in range(int(matrixCols)):
                            #now have row in userMatrix and first element of that row
                            #multiply element by item of first col in KEY and add to total
                            total += (int(userMatrix[row][col]) * int(keyMatrix[col][userCols]))
                        cipherText[row].append(total % len(charSet))
                        total = 0
                    #prevent an empty list from being appended at end of cipherText matrix
                    #add 1 to row because it counts at 0 and other operands count at 1
                    if (row+1 != int(matrixCols)) and (len(userMatrix) > row+1):
                        cipherText.append([])
            
            #next convert chars in cipherTextChars list to charSet values
            cipherText = convertToCharSet(cipherText)
            
            #output encryption
            output(K, TEXT, cipherText)
        elif mode == 'd':
            #get plainText matrix in decimal values
            plainText = []
            for plainRow in range(len(userMatrix)):
                plainText.append([])
                for item in range(len(inverseKey[0])):
                    getter = 0
                    for value in range(len(userMatrix[plainRow])):
                        getter += (int(userMatrix[plainRow][value]) * int(inverseKey[value][item]))
                    plainText[plainRow].append(getter % len(charSet))
            
            #next convert numbers in plainText to charSet character values
            plainText = convertToCharSet(plainText)
            
            #output decryption
            output(K, TEXT, plainText)
        
        #ask user if they would like to restart the program
        userExit = input('\nWould you like to encrypt/decrypt ' +
                         'another string? (Y)es or (N)o: ').lower()
        
        #make sure user only inputs Y or N
        while (userExit != 'y') and (userExit != 'n'):
            print('\nPlease only enter "Y" for yes and "N" for no.')
            userExit = input('Would you like to encrypt/decrypt ' +
                             'another string? (Y)es or (N)o: ').lower()
        
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
        print('\nYou\'ve entered an empty string, please enter an appropriate value.')
        input('Press ENTER to continue...')
        return False
    
    #check TEXT/KEY for any characters that are not in charSet
    for char in usrInput:
        if char not in charSet:
            print('\nIt looks like you\'ve used a character that is not acceptable.')
            print(' -Only use letters A - Z (uppercase + lowercase ' +
                    'will be treated the same).')
            print(' -Only use the numbers 0 - 9 (10 is counted ' +
                    'as two individual numbers).')
            print(' -Only use these special characters: ' +
                    '! " # $ % & \' ( ) * (exclude spaces).')
            input('Press ENTER to continue...')
            return False
                
    #return True to main to signify no errors in input
    return True

#function to concatenate a list of lists/blocks of characters into a string after 
#converting the individual chars to their corresponding charSet values
def convertToCharSet(usrInput):
    #concat the list of plaintext chars into one string
    #use first index of usrInput (userMatrix)
        #if user enters 2 chars then len of usrInput is only one, they fit into one block
        #user input is split into blocks of 2- to 3-element char lists, nested in a main list
    #len of first index (nested list) will give proper loop count
    for row in range(len(usrInput)):
        for col in range(len(usrInput[0])):
            #change the list of decimal values to their charSet values
            usrInput[row][col] = charSet[usrInput[row][col]]
            
    #userInput is a list of lists characters, concat them into one string and return it
    newText = ''
    tempText = ''
    for i in usrInput:
        tempText = tempText.join(i)
        newText += (tempText)
        tempText = ''
    return newText

#function to handle Euclidean GCD algorithm in order to find the inverse of
#the variable NUM in NUM mod MOD or the GCD(num, mod)
def findInverse(num, mod, returnGCD=False):
    #get inverse of num in (num % mod) where both arguments are integers
    #ax + by = gcd(a,b)
    a = num
    b = mod
    
    #x and y are used to start the X-side Euclidean GCD algorithm table as x0 = 1 and x1 = 0
    #x and y must switch values depending on which arg is larger to get correct output
    if num > mod:
        x = 0               #x0 = 0
        y = 1               #x1 = 1
    else:
        x = 1               #x0 = 1
        y = 0               #x1 = 0
    
    #this is the code for the Euclidean GCD algorithm
    while(b != 0):
        #find a # such that # * num <= mod (e.g. 6*7=42 <= 46 and 7*7=49 > 46)
        quotient = int(a) // int(b)
        #get the remainder of ((# * num) - mod)
        #e.g. ((7 * 6) - 46) = 4
        remainder = int(a) - (int(quotient) * int(b))
        #this equation is equivalent to x2 = -q1 * x1 + x0 from Euclidean GCD algorithm
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
    
    #return GCD instead of inverse if flag is specified as True in function call
    if returnGCD:
        return a
    
    #otherwise, x is the inverse of num so return that value
    return x

#function that gets determinant and adjoint matrices
def keyModify(keyMatrix, matrixCols):
    #get keyMatrix with row + col removed so determinant and adjoint can be found
    breakFlag = False
    determinant = 0
    adjoint = []
    for row in range(len(keyMatrix)):
        #add row to adjoint matrix, prevent unused rows from being added
        if breakFlag == False:
            adjoint.append([])
        else:
            break
        
        #adjoint will be transposed if 3x3 used, values adjusted differently in 2x2
        #"strike out" rows and cols as necessary
        if int(matrixCols) == 3:
            col = 0
            while (col < len(keyMatrix[row])):
                cofactor = []
                index = 0
                #cofactor has values not in keyMatrix[row] and not in keyMatrix[col]
                for item in range(len(keyMatrix)):
                    if (item != row):
                        cofactor.append([])
                        for value in range(len(keyMatrix[item])):
                            if (value != col):
                                cofactor[index].append(keyMatrix[item][value])
                        index += 1
                #get product of keyMatrix cofactor multiplication
                #product is made positive or negative based on row and col used
                a = cofactor[0][0]
                b = cofactor[1][1]
                c = cofactor[0][1]
                d = cofactor[1][0]
                matrixMulti = ((a * b) - (c * d)) * ((-1)**(row+1 + col+1))
                
                #accumulate determinant, requires only one row to find determinant, use first row
                #multiply each element in first row of key by cofactor product
                if (row == 0):
                    determinant += keyMatrix[row][col] * matrixMulti
                    breakFlag = False
                
                #add cofactor product to adjoint matrix
                adjoint[row].append(matrixMulti)
                
                #transpose matrix after adjoint is filled 
                #adjoint is filled when row and col are both equal to length of 
                #keyMatrix rows and cols
                if (row+1 == len(keyMatrix)) and (col+1 == len(keyMatrix[row])):
                    #transpose adjoint matrix, switch rows with cols
                    #could make this shorter by creating entire inverse key matrix in one line
                    #instead of transposed matrix then the inverse key matrix
                        #USE:     transpose[cols].append((det * int(rows[cols])) % len(charSet))
                        #REPLACE: transpose[cols].append(rows[cols])
                        #NOTE:    det = findInverse(determinant) % len(charSet) 
                        #         must come before loop
                    #may be useful to have algorithm that reads matrix + gives adjoint matrix
                    #so I chose this style because it's more portable
                    firstIteration = True
                    transpose = []
                    for rows in adjoint:
                        for cols in range(len(rows)):
                            #create 3 nested lists
                            #flag prevents creation of unused nested lists
                            if firstIteration == True:
                                transpose.append([])
                            transpose[cols].append(rows[cols])
                        if firstIteration == True:
                            firstIteration = False
                    adjoint = transpose
                
                #increment while counter
                col += 1
        elif int(matrixCols) == 2:
            #get determinant for 2x2, no striking out necessary
            if row == 0:
                a = keyMatrix[0][0]     #keyMatrix_1,1
                b = keyMatrix[1][1]     #keyMatrix_2,2
                c = keyMatrix[0][1]     #keyMatrix_1,2
                d = keyMatrix[1][0]     #keyMatrix_2,1
                #get determinant of keyMatrix - cross multiply
                determinant = (a * b) - (c * d)
            
            #get adjoint for 2x2 matrix (example 2x2 matrix called A)
            #swap values of A0-0 w/ A1-1 and vice versa
            #swap signs of A0-1 and A1-0, if A0-1 neg then make it pos and if A1-0 neg,
            #then make it pos, and vice versa
            adjoint.append([])
            adjoint[0].append(int(b))
            adjoint[0].append(-int(c))
            adjoint[1].append(-int(d))
            adjoint[1].append(int(a))
            breakFlag = True
            break

    #mod the determinant by length of the charSet
    determinant %= len(charSet)
    
    #multiply all items in adjoint by inverse of determinant
    #get the inverse of determinant
    detInverse = findInverse(determinant, len(charSet)) % len(charSet)
    inverseKey = []
    #gets inverse key matrix
    for row in range(len(adjoint)):
        inverseKey.append([])
        for col in adjoint[row]:
            inverseKey[row].append((detInverse * int(col)) % len(charSet))
    
    #find identity matrix for proof of key
    identity = []
    for identityRow in range(len(keyMatrix)):
        identity.append([])
        for row in range(len(keyMatrix)):
            value = 0
            for col in range(len(inverseKey)):
                #multiply rows of keyMatrix by columns of inverseKey matrix
                value += keyMatrix[identityRow][col] * inverseKey[col][row]
            identity[identityRow].append(value % len(charSet))
    
    return determinant, inverseKey, identity

#prints output for encryption and decryption
def output(KEY, PT, CT):
    #begin output for encryption
    print('\n\nHere are the variable details for this session:')
    print('      Nominal Values         Ordinal Values')
    print('\n    KEY  Input  PT/CT      KEY  Input  PT/CT')
    print('  ---------------------  ---------------------')
    item = 0
    while item in range(len(CT)):
        #print both nominal and ordinal value tables
        print('     ' + KEY[(item % len(KEY))] + '\t   ' + PT[item] + '      ' + CT[item] + 
             '        ' + str(charSet.index(KEY[(item % len(KEY))])).zfill(2) + 
             '     ' + str(charSet.index(PT[item])).zfill(2) + 
             '     ' + str(charSet.index(CT[item])).zfill(2))
        
        item += 1
    
    #if the KEY is longer than the TEXT and not all of the KEY is used, print unused values
    #only needed for KEY because the key matrix is either 2x2 or 3x3
    if (len(KEY) > len(PT)) and (len(KEY) > len(CT)):
        while item in range(len(KEY)):
            #print excess characters of KEY that weren't used in the algorithm
            #prints appropriate values for both tables
            print('     ' + KEY[(item % len(KEY))] + '\t   -      -        ' + 
            str(charSet.index(KEY[(item % len(KEY))])).zfill(2) + 
            '     --     --')
           
            item += 1
    #print one last blank line for readability
    print()

main()
