#630510582
#tulakorn sawangmuang
#Section-001
#Lab04-04
#Mathematical rounding

import math
 
def round_to_int(x):
    y = (math.floor(x)) #Equation y
    if x >= 0: #Configure
        if x - y >= 0.5: #condition
            x = y + 1 # x value
        else: # Beyond the condition
            x = y # x value
    u = (math.ceil(x)) #Equation u
    if x < 0: #Configure
        if abs(x - u) >= 0.5: #condition
            x = u - 1 # x value
        else: #Beyond the condition
            x = u # x value
    return x #return x to this function

def main():
    x = float(input("")) # get number from user input
    answer = round_to_int(x) #Equation answer
    print("{0}".format(answer)) #Answer

if __name__ == "__main__":
    main()