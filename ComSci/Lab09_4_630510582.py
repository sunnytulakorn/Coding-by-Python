#630510582
#tulakorn sawangmuang
#Section-001
#Lab09_4

def series(n):
    if n == 0: # base case 
        return 0 
    if (n-1)%2 == 1 or n == 1: # condition
        return 2*series(n-1)+1 # call function if n is even
    else:
        return 2*series(n-1)-1 # call function if n is odd

def main():
    n = int(input()) # input n
    print(series(n)) # display answer

if __name__ == "__main__":
    main()
    
