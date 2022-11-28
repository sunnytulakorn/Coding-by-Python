import math

def show_series(a, b):
    if(a != b and a >= 0 and b >= 0):
        if(a < b):
            for i in range(a, b+1):
                print(i)
                i += 1
        if(a > b):
            for i in range(a, b-1, -1):
                print(i)
                i += 1
    else:
        print("0")


def main():
    a = int(input())
    b = int(input())
    show_series(a, b)
    main()

if __name__=="__main__":
    main()