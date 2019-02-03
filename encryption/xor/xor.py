global TEXT

charSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*']

def main():
    print('\n\nAssignment 1 - Encrypt or Decrypt\n\n')
    
    #ask user if they want to ENCRYPT or DECRYPT
    print('Enter an E to encrypt your plaintext string.')
    print('Enter a D to decrypt your cyphertext string.', end='')
    mode = input('(E)ncrypt or (D)ecrypt: ').lower()
    
    #check for correct input
    while (mode != 'e') and (mode != 'd'):
        print('\n\nPlease only enter an E or a D.', end='')
        mode = input('(E)ncrypt or (D)ecrypt: ').lower()
    if mode == 'e':
        print('\n\nYou\'ve chosen to ENCRYPT your palintext string.', end='')
        PT = input('Enter the plaintext string you\'d like to ENCRYPT: ').lower()
        
        #set global variable TEXT to user input so only one variable needs to be manipulated
        TEXT = PT
    elif mode == 'd':
        print('\n\nYou\'ve chosen to DECRYPT your cyphertext string.', end='')
        CT = input('Enter the cyphertext string you\'d like to DECRYPT: ').lower()
        
        #set global variable TEXT to user input so only one variable needs to be manipulated
        TEXT = CT
    
    #check input for errors
    if not errorCheck(TEXT):
        #if the program enters this block it means that TEXT has a character that's not in charSet
        return
    
    #get KEY from user
    print('\n\nNow you must enter a KEY string that is used to encrypt or decrypt the string you entered.')
    print('The KEY must be the same length as the string that will be encrypted/decrypted.')
    print('This means that the two strings should have the same number of characters.')
    print('However, the KEY must NOT be the same string as the PLAINTEXT OR CYPHERTEXT.', end='')
    K = input('Please input a KEY: ').lower()
    
    #error check KEY
    if (len(K) != len(TEXT)) or (K == TEXT):
        while (len(K) != len(TEXT)) or (K == TEXT):
            print('\n\nYou either entered a KEY that was not the same length as the PLAINTEXT or CYPHERTEXT string,\n',
                  'or a KEY that\'s identical to the PLAINTEXT or CYPHERTEXT.')
            print('Make sure the KEY is the same number of characters as the PLAINTEXT string.')
            print('The KEY must not be the same string as PLAINTEXT or CYPHERTEXT.', end='')
            K = input('Please enter another KEY: ').lower()
    if not errorCheck(K):
        #if the program enters this block it means that K has a character that's not in charSet
        return
    
    #convert TEXT (which is PT or CT) into binary and decimal values
    binText = []
    decText = []
    for char in TEXT:
        decText.append(charSet.index(char))
    for num in decText:
        converted = bin(num)
        binText.append(converted.replace('b', '').zfill(8))
    
    #convert K to binary for XORing the PT or CT with K
    binKey = []
    decKey = []
    for char in K:
        decKey.append(charSet.index(char))
    for num in decKey:
        converted = bin(num)
        binKey.append(converted.replace('b', '').zfill(8))
    
    #now do PT XOR K or CT XOR K
    compare = []        #holds XOR value of individual bits in the bytes for each character of input
    xorBinText = []     #holds XOR'd byte for each character of input
    xorByte = ''        #variable used to store all XOR'd bits from compare list as one byte instead of a list of 8 bits
    for byte in range(len(binText)):
        #reset list and string after each byte is XOR'd
        compare = []
        xorByte = ''
        for bit in range(len(binText[byte])):
            if binKey[byte][bit] == binText[byte][bit]:
                compare.append('0')
            else:
                compare.append('1')
        xorBinText.append(xorByte.join(compare))
    
    #convert the XOR'd bytes for each character into decimal numbers
    xorDecText = []
    for byte in range(len(xorBinText)):
        #loop grabs an individual byte from the list of XOR'd bytes
        #set a total variable to compute the decimal value of the individual bytes
        #set a bitPosition so it maintains bit position in byte since byte is read right to left - rightmost bit is 0 bitPosition
        total = 0
        bitPosition = 0
        for bit in range((len(xorBinText[byte])-1), -1, -1):
            #take each bit of the byte, from rightmost bit to leftmost bit, and if the bit is 1 then add 2^bit to a total
            if xorBinText[byte][bit] == '1':
                total += 2**bitPosition
            bitPosition += 1
        xorDecText.append(total)
    
    #convert decimal values for the XOR'd bytes and match them to the corresponding characters in charSet
    #variable to hold character values of XOR'd bytes
    #represents both PT and CT because each was set to a global TEXT variable after user decides whether or encrypt or decrypt
    xorOutput = []
    for num in xorDecText:
        xorOutput.append(charSet[(num % 46)])
    
    #output - changes if user is encrypting or decrypting    
    if mode == 'e':
        print('\n\nPT =', TEXT)
        print('K =', K)
        print('PT\tK\tCT\tDec\t Binary')
        print('------------------------------------------')
        for i in range(len(TEXT)):
            print(str(TEXT[i]) + '\t' + str(K[i]) + '\t' + str(xorOutput[i]) + '\t ' + str(xorDecText[i]) + '\t' + str(xorBinText[i]))
    elif mode == 'd':
        print('\n\nCT =', TEXT)
        print('K =', K)
        print('CT\tK\tPT\tDec\tBinary')
        print('------------------------------------------')
        for i in range(len(TEXT)):
            print(str(TEXT[i]) + '\t' + str(K[i]) + '\t' + str(xorOutput[i]) + '\t ' + str(xorDecText[i]) + '\t' + str(xorBinText[i]))

#function for checking if input is in charSet
def errorCheck(usrInput):            
    #check PT for any characters that are not in charSet
    for char in usrInput:
        if char not in str(charSet):
            print('\n\nIt looks like you\'ve used a character that is not acceptable.')
            print('Please only use letters A - Z (uppercase and lowercase will be treated the same).')
            print('Please only use the numbers 0 - 9 (10 will be counted as two individual numbers).')
            print('Please only use these special characters: ! " # $ % & \' ( ) * (exclude spaces).')
            return False
    
    #return True to main to signify no errors in input
    return True
main()
