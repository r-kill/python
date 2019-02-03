'''
Chinese Remainder Theorem
Rowan Kill
Resubmission 4/15/17
'''

def main():
    print('\n\nAssignment 4 - Chinese Remainder Theorem')
    #print user info and show menu, get input, then error check that input
    print('\nAttempt to solve two equations using the Chinese Remainder Theorem (CRT)!')
    print(' -You will enter the values for two modulous equations, (a mod m) and (b mod n).')
    print(' -These values will represent A, M, B, and N.')
    print(' -With proper values, the equations can be solved simultaneously via the CRT.')
    print(' -Proper values for M and N are values in which the gdc(m, n) = 1.')
    print(' -In other words, the values for M and N must be relatively prime to one another.')
    print(' -However, M cannot be equivalent to N.')
    input('Press ENTER to continue...')
    print('\n\nPlease only input either START (start the program) or EXIT (exit the program).')
    print(' -Your input can be uppercase or lowercase.')
    
    #create flag to loop menu in case user exits, but then decides against exiting
    #flag never needs to change because program exits completely or breaks out of loop
    regretExit = True
    while regretExit != False:
        menuOption = input('\nWould you like to START or EXIT: ').lower()
        while (menuOption != 'exit') and (menuOption != 'start'):
            print('\nPlease only input the words START or EXIT, uppercase or lowercase.')
            menuOption = input('Would you like to START or EXIT: ').lower()
        
        #if user wants to exit, verify and either exit or go back to main menu
        if menuOption == 'exit':
            checkExit = input('\nAre you sure you want to exit? (Y)es or (N)o: ').lower()
            while (checkExit != 'y') and (checkExit != 'n'):
                print('\nPlease only enter Y for yes or N for no, uppercase or lowercase.')
                checkExit = input('Are you sure you want to exit? (Y)es or (N)o: ').lower()
            if checkExit == 'y':
                print('\n\nThank you for using this program.\n')
                return
            else:
                input('Press ENTER to go back to the main menu...')
                continue
        else:
            break
        
    #create a flag that controls where program loops to if user doesn't exit after first run
    endChoice = ''
    #check for errors and get new input if user chooses correct endChoice option
    errorFlag = True
    while errorFlag:
        #get A, M, B, N from user
        print('\n\nEnter each variable for A mod M and B mod N individually.')
        print(' -REMEMBER: The value for M must be relatively prime to the value for N.')
        #if user chooses to use output as new A and M values, this must be skipped
        if endChoice != 'a':
            print('\nFor A mod M:')
            A = input(' -Enter a value for variable A: ').lower()
            M = input(' -Enter a value for variable M: ').lower()
        else:
            print('\nA mod M ==', A, 'mod', M)
            print('    A =', A)
            print('    M =', M)
        print('\nFor B mod N:')
        B = input(' -Enter a value for variable B: ').lower()
        N = input(' -Enter a value for variable N: ').lower()
        errorCheck = [A, M, B, N]
        
        #check input
        #set flag to false initially so blocks can be skipped as needed
        errorFlag = False
        for i in errorCheck:
            #strip any hyphens (-) to prevent negative nums from being blocked
            if i.strip('-').isnumeric() != True:
                print('[ERROR] - Please only input numbers for A, M, B, and N.')
                errorFlag = True
                break
        errorCheck.clear()
        #if an input isn't numeric, try to get gcd
        #if non-numeric input is N or M, taking int(N) or int(M) will error due to non-numeric
        #get gcd if possible, not necessary, if it fails that value will be caught by isnumeric()
        try:
            if (findInverse(int(M), int(N), True) != 1) or (M == N):
                print('[ERROR] - Please make sure that the values for M and N are relatively prime.')
                print(' -This means that the gcd(m, n) = 1. It also means that M != N.')
                errorFlag = True
        except:
            pass
        if errorFlag == True:
            print('\nPlease enter new values for A, M, B, and N. Check the error messages above.')
            input('Press ENTER to go back to input menu...')
            continue
    
        #CRT
        #convert from A mod M to ((A  mod M) + M*k) = B mod N
        #x = (A mod M)
        x = int(A) % int(M)
        #subtract x from B so we get M*k alone
        tempB = int(B)
        tempB -= x
        #if B == 0, then k = 0
        #if B < 0, take mod of it so B is positive
        if int(tempB) == 0:
            k = 0
            #since k = 0 and equation is x + M*k, result is just x
            result = x
        else:
            #if B is negative this makes it positive
            tempB = int(tempB) % int(N)
            #now we have M*k = B mod N, so we need to find inverse on M mod N and multiply
            #this is how we find k in M*k
            inverseM = findInverse(int(M), int(N))
            k = (int(inverseM) * int(tempB)) % int(N)
            result = int(x) + int(M) * int(k)
        
        #output
        print('\n\n    INPUT\t  OUTPUT')
        print('--------------------------------')
        print(' ', A.zfill(2), 'mod', M.zfill(2) + '\t' + str(result).zfill(2), 'mod', (int(M) * int(N)))
        print(' ', B.zfill(2), 'mod', N.zfill(2))
        print()
        
        #ask user if they want to continue with more equations
        print('\nDo you want to:')
        print('\t(A) - Use the output values for a new A and M,')
        print('\t      then input new values for B and N.')
        print('\t(B) - Input a full set of new values (A, M, B, and N).')
        print('\t(C) - Exit the program.')
        endChoice = input('\nPlease input one of the letters from the list above: ').lower()
        while (endChoice != 'a') and (endChoice != 'b') and (endChoice != 'c'):
            print('\nDo you want to:')
            print('\t(A) - Use the output values for a new A and M,')
            print('\t      then input new values for B and N.')
            print('\t(B) - Input a full set of new values (A, M, B, and N).')
            print('\t(C) - Exit the program.')
            print('\nPlease only enter one of the letters shown in the list.')
            endChoice = input('Please input one of the letters from the list above: ').lower()
        
        if endChoice == 'a':
            #set output function as new A and M values
            A = str(result)
            M = str(int(M) * int(N))
            #set errorFlag to true in order to loop through program again
            errorFlag = True
        elif endChoice == 'b':
            #set errorFlag to true in order to loop through program again
            errorFlag = True
        elif endChoice == 'c':
            #ask user if they are sure they want to exit and then exit or start over
            checkExit = input('\nAre you sure you want to exit? (Y)es or (N)o: ').lower()
            while (checkExit != 'y') and (checkExit != 'n'):
                print('\nPlease only enter Y for yes or N for no, uppercase or lowercase.')
                checkExit = input('Are you sure you want to exit? (Y)es or (N)o: ').lower()
            if checkExit == 'y':
                print('\n\nThank you for using this program.\n')
                return
            else:
                input('Press ENTER to go back to the input menu...')
                errorFlag = True
                continue

#function to handle Euclidean GCD algorithm in order to find the inverse of
#the variable NUM in NUM mod MOD or the GCD(num, mod)
def findInverse(num, mod, returnGCD=False):
    #get inverse of num in (num % mod) where both arguments are numbers
    #ax + by = gcb(a,b)
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
    
    #return GCD instead of inverse
    if returnGCD:
        return a
    
    #now x is the inverse of num so return that value
    return x

main()
