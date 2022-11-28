#630510582
#tulakorn sawangmuang
#Section-001
#Lab06_1

def int_power(x, y):
    x != 0 # define x
    result = 1 # value
    if y > 0: # condition to join this loop
        for i in range(y): # loop
            result *= x # multiply x to value
    
    if y < 0: # another condition to join this loop
        for i in range(abs(y)): # #loop
            result *= 1/x # multiply 1/x to value

    return result # answer

def main():
    x = float(input("")) # input x value
    y = int(input("")) # input y value
    answer = int_power(x, y) # equation answer
    print("{0}".format(answer)) # show the answer

if __name__ == "__main__":
    main()

