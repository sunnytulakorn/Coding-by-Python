import math

def leap_year(y, m):
    feb = 0

    if( y % 4 == 0):
        if(y % 100 == 0):
            if(y % 400 == 0):
                print("Leap Year")
                feb += 29
            else:
                print("Non Leap Year")
                feb += 28
        else:
            print("Leap Year")
            feb += 29
    else:
        print("Non Leap Year")
        feb += 28
    
    if(m == 1):
        print("31")
    elif(m == 2):
     print(feb)
    elif(m == 3):
        print("31")
    elif(m == 4):
        print("30")
    elif (m == 5):
        print("31")
    elif(m == 6):
        print("30")
    elif(m == 7):
        print("31")
    elif(m == 8):
        print("31")
    elif(m == 9):
        print("30")
    elif(m == 10):
        print("31")
    elif(m == 11):
        print("30")
    elif(m == 12):
        print("31")


def main():
    y = int(input())
    m = int(input())
    leap_year(y, m)
    main()

if __name__=="__main__":
    main()