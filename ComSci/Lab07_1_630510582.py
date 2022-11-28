#630510582
#tulakorn sawangmuang
#Section-001
#Lab07_1
import math

def sum_prime_in_range(x,y):
    result = 0 # value
    for i in range(x, y+1): # loop
        if isPrime(i): # prime value
            result += i #plus prime value
    return result # return value

def isPrime(num):
    if num < 2: #number > 2 do this
        return False #display
    for k in range(2, num): # loop
        if num % k == 0: # condition
            return False # display
    return True # display

def main():
    x = int(input()) # input the value
    y = int(input()) # input the value
    print(sum_prime_in_range(x,y)) # display value

if __name__ == "__main__":
    main()

