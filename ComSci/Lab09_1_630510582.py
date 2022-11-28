#630510582
#tulakorn sawangmuang
#Section-001
#Lab09_1

def gcd(x, y):
    if y == 0: # base case
        return x
    else: # calling gcd function to find gcd
        return gcd(y, x%y)

def main():
    x = int(input()) # input number
    y = int(input()) # input number
    print(gcd(x, y)) # display 

if __name__ == "__main__":
    main()