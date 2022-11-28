#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab04_5

def triangle(n):
    k = 0
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            print(end=" ")
        
        while k != (2*i-1):
            print("*", end="")
            k += 1
        
        k = 0
        print()
        
def main():
    n = int(input("Enter star number: "))
    triangle(n)

if __name__=="__main__":
    main()