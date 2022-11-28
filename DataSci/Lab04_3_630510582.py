#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab04_3
import math

def prime_factorization(n):
    if check_prime(n):
        print("%d"%(n))
    else:
        i = 2
        while i <= (math.sqrt(n)):
            if n % i == 0:
                n //= i
                print(i)
            else:
                if i > 2:
                    i += 2
                else:
                    i += 1
        print(n)


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
    n = int(input("Enter n: "))
    prime_factorization(n)

if __name__=="__main__":
    main()
