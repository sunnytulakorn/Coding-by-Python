#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab01_1

def fncal_area(n):
    square = n*n #square equation
    circle = (3.141593)*((n/4)**2) #circle equation
    circle_4 = circle*4 #have 4 circle in square
    shadow = square - circle_4 #shadow value
    print("%.2f\n%.2f\n%.2f"%(square,circle,shadow)) 

def main():
    n = int(input())
    fncal_area(n)

if __name__ == "__main__":
    main()