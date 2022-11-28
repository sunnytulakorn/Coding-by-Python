#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab05_4

def count_prime(m, n):
    m = int(m)
    n = int(n)
    keepValue = 0
    count = 0
    if(m > n):
        keepValue = m
        m = n
        n = keepValue

    for i in range(m, n+1):
        if check_prime(i):
            count += 1
    
    return count

def check_prime(n):
    t = 0
    for i in range(1, n+1):
        if n % i == 0:
            t += 1
            if t > 2:
                break
    if t > 2:
        return False
    else:
        return True

def main():
    m, n = (input("Enter m n: ")).split(" ")
    ans = count_prime(m, n)
    print(ans)
    main()

if __name__=="__main__":
    main()