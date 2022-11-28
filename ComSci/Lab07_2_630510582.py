#630510582
#tulakorn sawangmuang
#Section-001
#Lab07_2

import math

def digit_count(x, base=10):
    result = 1 # define result
    while abs(x)//base > 0: # condition do this loop
        x = abs(x)//base # x value
        result += 1 # plus 1 to value
    return result #display the value


def main():
    x = int(input()) # input value
    y = int(input()) # input value
    print(digit_count(x, y)) # display value

if __name__ == "__main__":
    main()