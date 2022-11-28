#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab02_3

import math

def fncal_all_area(n) :
    square = n*n
    big_c = n/2
    circle = fncal_cycle_area(big_c)
    r_small = (n/8)*(math.sqrt(2)-1)
    c_small = fncal_cycle_area(r_small)*3
    shadow = square - circle - c_small
    print("%.2f\n%.2f\n%.2f\n%.2f"%(square,circle,c_small,shadow))

def fncal_cycle_area(r):
    return(math.pi*r*r)

def main():
    n = int(input())
    fncal_all_area(n)

if __name__=="__main__":
    main()