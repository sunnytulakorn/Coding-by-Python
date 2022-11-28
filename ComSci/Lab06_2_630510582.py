#630510582
#tulakorn sawangmuang
#Section-001
#Lab06_2

import math

def float_to_bin(x):
    result = 0 # value
    a = abs(x) # define a value
    if type(x) == int or type(x) == float : #condeition to join this loop
        if type(x) == float:#2nd condition to join this loop
            i = 0 # define i
            while a != 0: #stop when a=0
                b = a                                                    #equation
                a = b//2 #equation
                r = b%2 #equation
                result += (r*(10**i)) #add this value in result value
                i += 1 #plus 1 to i 
                answer = result//1 # don't take decimal
                ANSWER = answer # bin value but don't have decimal
        
        if type(x**2) == float: # another condition to join this loop 
            a = abs(x) # define a value
            z = a - (math.floor(a)) # define z value
            i_order = -1 # define i_order
            result1 = 0 # value
            for m in range (6): # do 6 time
                z = z*2 # equation
                c = z//1 # equation
                z %= 1 # equation
                result1 += (c*(10**i_order)) # add this value in result1 value
                i_order -= 1 #minus 1 to i_order
                ANS = result1 # bin value for decimal
    if x<0: # condition
        return -(ANSWER + ANS) #answer
    if x>0: # condition
        return ANSWER + ANS # answer
    if x == 0: # condition
        return ANS # answer

def main():
    x = float(input()) # input the number
    number = float_to_bin(x) # equation
    print("%.6f"%(number)) #show the answer

if __name__ == "__main__":
    main()