#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab05_1

def multiple_table(n):
    if (1 <= n <= 12):
        for i in range(1, n+1): #row
            for k in range(1, n+1): # column
                print("%4d"%(k*i), end="")
            print('')

    else:
        print("Invalid Input")

def main():
    n = int(input("Enter n: "))
    multiple_table(n)
    main()

if __name__=="__main__":
    main()