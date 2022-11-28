#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab04_4

def xy_factors(x, y, n):
    count = 0
    for i in range(1, n+1):
        if i % x == 0:
            count += 1
        elif i % y == 0:
            count += 1
    return count

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    n = int(input("Enter n: "))
    ans = (xy_factors(x, y, n))
    print(ans)

if __name__=="__main__":
    main()