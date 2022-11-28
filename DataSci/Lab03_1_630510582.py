#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab03_1

def divide_3and5(n):
    if (n%3 == 0 and n%5 == 0):
        return ("Both")
    elif (n%3 == 0):
        return ("Three")
    elif (n%5 == 0):
        return ("Five")
    else:
        return ("None")
    

def main():
    n = int(input("Enter number: "))
    ans = divide_3and5(n)
    print(ans)
    main()

if __name__=="__main__":
    main()