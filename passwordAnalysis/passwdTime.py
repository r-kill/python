from time import *

# guideline flags
hasEightChar = False   # may not need this variable
hasUpperCase = False
hasLowerCase = False
hasNums = False
hasSpecialChar = False # one of these: ? . [ ] { } - _ ! * + ~

# make sure passwd doesn't contain %
# initial assumption is that password does NOT contain a %
noPercent = True

# create an array containing the special chars
specials = ['?', '.', '[', ']', '{', '}', '-', '_', '!', '*', '+', '~']
    
avg = 0         # average time to authenticate
count = 0       # count passwords that have been authenticated
elapsed = 0     # time it took to process password

# user info
print('This program checks if passwords read from a file are acceptable or not.')
print('The file should be in the same folder as the program.')
print('An acceptable password:')
print('\t[+] has eight or more characters' +
      '\n\t[+] includes lowercase and uppercase letters' +
      '\n\t[+] includes numbers' +
      '\n\t[+] includes at least one of these characters: ? . [ ] { } - _ ! * + ~' +
      '\n\t[+] DOES NOT include a \'%\' character', end='\n\n')

# open passwords file for reading
file = open('13000passwords.txt')

# get password from file one line at a time
p = file.readline()

#get current time from time lib
t1 = clock()

while(p != ''):
    #start testing password
    if(len(p) >= 8):
        # set length flag to true
        hasEightChar = True
        
        # check for % character in password
        x = p.find('%')
        if(x == -1):
            # iterate through passwd and check each character
            for i in range(len(p)):
                char = p[i]
                if(hasUpperCase == False and char.isupper()):
                    # set flag to true for uppercase letters
                    hasUpperCase = True
                elif(hasLowerCase == False and char.islower()):
                    # set flag to true for lowercase letters
                    hasLowerCase = True
                elif(hasNums == False and char.isnumeric()):
                    # set flag to true for numbers in password
                    hasNums = True
            
            # check password for special chars last, otherwise it ends up
            # looping through the password multiple times for no reason
            # only check for special chars if there's no % in the password
            # (that makes it a bad password so no point in continuing to check it)
            if(hasSpecialChar == False):
                # loop through list of special chars and
                # compare them to chars in the password
                # if one special char is found in the password,
                # no need to keep checking for others
                for i in range(len(specials)):
                    if(specials[i] in p):
                        hasSpecialChar = True
                        break
        else:
            # set flag to false to signify that there is a % in the password
            noPercent = False
        
        # if all flags are true, password fits criteria for a good password
        # report the time it took to determine that it's a good password
        # noPercent will be False if it DOES exist in the password
        if(hasUpperCase == True and hasLowerCase == True and
           hasNums == True and hasSpecialChar == True and noPercent == True):
            elapsed = clock() - t1
            #print('[+] Good password:  Comparison time: {0:.15f}'.format(elapsed))
            avg += elapsed
        else:
            # report time it took to determine password was bad
            elapsed = clock() - t1
            #print('[-] Bad password:    Comparison time: {0:.15f}'.format(elapsed))
            avg += elapsed
    else:
        # output check time
        elapsed = clock() - t1
        #print('[-] Bad password:    Comparison time: {0:.15f}'.format(elapsed))
        avg += elapsed

    # reset guideline flags
    hasEightChar = False   # may not need this variable
    hasUpperCase = False
    hasLowerCase = False
    hasNums = False
    hasSpecialChar = False # one of these: ? . [ ] { } - _ ! * + ~
    noPercent = True       # make sure passwd doesn't contain %

    # increment count
    count += 1
    
    #get next password
    p = file.readline()

    #get current time from time lib
    t1 = clock()

# close passwords file
file.close()

# report average password calculation time
print('Average time {0} passwords were analyzed: {1:.15f}'.format(count, avg / count))
