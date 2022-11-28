#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab02_4

import math

def fncal_shaded_area(a, b):
    a = float(a)
    b = float(b)
    shadow = square_area(a) - triangle_area(a, b)
    tri_ = triangle_area(a, b)
    print("%.2f %.2f"%(tri_,shadow))

def square_area(a):
    return(a*a)

def triangle_area(a, b):
    return((a/4)*math.sqrt((4*(b**2))-(a**2)))

def main():
    a,b = input().split(',')
    fncal_shaded_area(a, b)
    main()

if __name__=="__main__":
    main()