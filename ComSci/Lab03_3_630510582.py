#630510582
#tulakorn sawangmuang
#section-001
#Lab03-03
#find octagon area
import math

def octagon_area(x):
    area = x * x #Equation of Parallelogram area
    tri = (1/2)*(x/3)*(x/3) #Equation Area of ​​Triangle
    octagonarea = area - (4*(tri)) #Equation of octagon area
    return octagonarea #return octagonarea value to this function

def main():
    x = float(input("")) #get x from user input
    octagonarea = octagon_area(x) #display octagonarea
    print ("octagon area={0:.2f}".format(octagonarea)) #Answer

if __name__ == "__main__":
    main()