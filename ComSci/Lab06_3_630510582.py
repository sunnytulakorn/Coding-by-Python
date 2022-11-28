#630510582
#tulakorn sawangmuang
#Section-001
#Lab06_3

import math

def factorize(x):
    if is_prime(x): # condition to join this loop
        print ("%d is prime"%(x)) # display prime
    else: # other condition
        i = 2 # define i
        print("%d is "%x,end ="") # display 
        while i <= (math.sqrt(x)): # condition to do this loop when i <= (math.sqrt(x))
            if x % i == 0: # condition
                x = x//i # define
                print(i,"*",end =" ") # display
            else: # other condition
                if i > 2: # condition 
                    i = i + 2 # equation
                else: # other condition
                    i = i + 1 # equation
        print(x) # display

def is_prime(x):
    t = 0 # define t 
    for i in range(1, x+1): #loop
        if x % i == 0: # condition
            t = t + 1 # equation
            if t > 2: # condition
                break # stop loop
    if t > 2: # condition 
        return False # display
    else: # other condition
        return True # display

def main():
    x = int(input()) # input x value
    factorize(x) # answer
   
if __name__ == '__main__':
    main()