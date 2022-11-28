#630510582
#tulakorn sawangmuang
#Section-001
#Lab12_3
import math
def prime_factor(n):
    answer = factorize(n) # call function
    return answer

def factorize(x):
    ans = [] # answer 
    if is_prime(x): # condition to join this loop
        ans += [x] 
    else: # other condition
        i = 2 # define i
        while i <= (math.sqrt(x)): # condition to do this loop when i <= (math.sqrt(x))
            if x % i == 0: # condition
                x = x//i # define
                ans += [i]
            else: # other condition
                if i > 2: # condition 
                    i = i + 2 # equation
                else: # other condition
                    i = i + 1 # equation
        ans += [x]
    return ans # display

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

def factorize1(b):
    ans1 = [] # answer 2nd 
    if is_prime(b): # condition to join this loop
        ans1 += [b] 
    else: # other condition
        i = 2 # define i
        while i <= (math.sqrt(b)): # condition to do this loop when i <= (math.sqrt(x))
            if b % i == 0: # condition
                b = b//i # define
                ans1 += [i]
            else: # other condition
                if i > 2: # condition 
                    i = i + 2 # equation
                else: # other condition
                    i = i + 1 # equation
        ans1 += [b]
    return ans1 # display

def is_prime1(b):
    t = 0 # define t 
    for i in range(1, b+1): #loop
        if b % i == 0: # condition
            t = t + 1 # equation
            if t > 2: # condition
                break # stop loop
    if t > 2: # condition 
        return False # display
    else: # other condition
        return True # display

def coprime_factor(a, b):
    f = prime_factor(a)
    h = factorize1(b)
    ans = []
    if len(f) > len(h): 
        for i in h:
            if i in f: # run list
                ans += [i]
                f.remove(i) # remove value
    else:
        for j in f:
            if j in h: # run list
                ans += [j]
                h.remove(j) # remove value
    return ans

def main():
    n = int(input())
    b = int(input())
    print(prime_factor(n))
    print(coprime_factor(n, b))

if __name__ == "__main__":
    main()