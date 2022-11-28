#630510582
#tulakorn sawangmuang
#Section-001
#Lab04-05
#Return value when even or odd numbers
import math

def nearest_odd(x): 
    x = (math.floor(x)) #Equation x
    if x%2 == 0: #Configure
        x = x+1 # x value
    if x%2 != 0: #Configure
        x = x # x value
    return x #return x to this function

def main():
    x = float(input("")) #get number from user input
    answer = nearest_odd(x) #Equation answer
    print("{0}".format(answer)) #Answer

if __name__ == "__main__":
    main()