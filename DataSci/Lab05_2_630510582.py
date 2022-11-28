#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab05_2

def print_triangle(n, type):
    if(type == "U"):
        if(n >= 0):
            for i in range(n): #row
                for k in range(i+1):
                    print(k+1, end='')
                print('')
        if(n < 0):
            n *= -1
            run = n
            for a in range(1, n+1): #row
                for b in range(a): #column
                    print(run, end='')
                    run -= 1
                print('')
                run = n

    elif(type == "D"):
        if(n >= 0):
            for i in range(n, 0, -1): #row
                for k in range(i): # column
                    print(k+1, end='')
                print('')

        if(n < 0):
            n *= -1
            count = 0
            run = n
            for i in range(n, 0, -1): #row
                run -= count
                for k in range(i): # column
                    print(run, end='')
                    run -= 1
                print('')
                run = n
                count += 1

def main():
    n = int(input("Enter n: "))
    type = input("Enter U or D: ")
    print_triangle(n, type)
    # main()

if __name__=="__main__":
    main()