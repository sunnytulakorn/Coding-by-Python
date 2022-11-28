#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab01_2

def fncal_shade_area(n):
    square = 3*n*n #square equation
    circle = 3*(3.141593)*((n/4)**2) #circle equation
    circle_4 = circle*4 #have 4 circle in square
    shadow = square - circle_4 #shadow value
    print("%.2f"%(shadow))

def main():
    n = int(input())
    fncal_shade_area(n)
    main() # recursive main
if __name__ == "__main__":
    main()