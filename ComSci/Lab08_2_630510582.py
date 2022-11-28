#630510582
#tulakorn sawangmuang
#Section-001
#Lab08_2

import string

def is_palindrome(x, b):
    2 <= b <= 9 # condition
    a = abs(x) 
    result = 0 
    i = 0 # run i in loop
    while a != 0: 
        s = a % b
        result += s * (10**i)
        i += 1 # plus to run i in this loop
        a = a // b # next value

    result = str(result) # change int to string
    if len(result)%2 == 0: # condition when is even number
        q = result[:(len(result)//2)] # Left half
        p = result[-1*(len(result)//2):] # right half
        z = p[len(p)::-1] # reverse right half 
        if int(z) == int(q): # change to int for compare the value
          return True
        else:
            return False
    
    elif len(result)%2 != 0 and len(result) != 1: # condition when is odd number and not 1
        j = result[:(len(result)//2)] # left half
        k = result[-1*((len(result)//2)):] # right half
        l = k[len(k)::-1] # reverse right half
        if int(j) == int(l): # change to int for compare the value (not middle value)
            return True
        else:
            return False

    if len(result) == 1: # condition when is 1
        m = result[:len(result)] # left half
        n = result[-1*(len(result)):] # right half
        if int(m) == int(n): # change to int for compare the value
            return True
        else:
            return False

def main():
    x = int(input()) # input value
    y = int(input()) # input value
    print(is_palindrome(x, y)) # answer
    main()

if __name__ == "__main__":
    main()