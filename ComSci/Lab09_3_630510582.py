#630510582
#tulakorn sawangmuang
#Section-001
#Lab09_3
import math
def  is_prime(n):
    return prime_x(n, 2) # call function to display answer

def prime_x(n, x): # creat function to add another variable for easy to find prime
    if math.floor(n**(1/2))+1 == x: # base case 
        return True # display
    else: 
        if n%x == 0: # base case
            return False # display
        return prime_x(n, x+1) # call function and run value

def main():
    n = int(input()) # input n
    print(is_prime(n)) # display answer
    main()

if __name__ == "__main__":
    main()
