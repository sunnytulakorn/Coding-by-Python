#630510582
#tulakorn sawangmuang
#Section-001
#Lab07_5

def rotate(num, pos):
    first = 0 # first value
    second = 0 # second value
    x = digitnext(num)-1 # x value equation
    if 0 != pos > 0: # condition
        for i in range(1, pos+1): # loop
            second = num % 10 # second value
            first = num // 10 # first value
            forth = second * (10**x) # forth value
            num = forth + first # num value
        return abs(num) # display value
    else: # another condotion
        pos = abs(pos) # pos value
        for i in range(1, pos+1): #loop
            second = num % 10**x # second value
            forth = second * 10 # forth value
            y = num - second # y value
            first = y // 10**x # update first value
            num = forth + first # num value
        return abs(num) # display value

def digitnext(num):
    z = 0 # z value
    y = num # y valus is num 
    while y > 0: # condition to do this loop
        y = y // 10 # y value
        z += 1 # plus 1 to z when do this loop
    return abs(z) # display value

def main():
    num = int(input()) # input value
    pos = int(input()) # input value
    print(rotate(num, pos)) #display value

if __name__ == "__main__":
    main()
        

