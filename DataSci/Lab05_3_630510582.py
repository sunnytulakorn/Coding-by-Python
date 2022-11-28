#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab05_3

def divide_3or7(m, n):
    m = int(m)
    n = int(n)
    last_number = None
    div_3 = 0
    div_7 = 0
    value_3 = 0
    value_7 = 0

    for i in range(m, n+1):
        if(i%3 == 0):
            div_3 += 1
            value_3 = i
        if(i%7 == 0):
            div_7 += 1 
            value_7 = i
    if(value_3 > value_7):
        last_number = value_3
    elif(value_3 < value_7):
        last_number = value_7
    else:
        last_number = None
        
    return last_number,div_3,div_7


def main():
    m, n = (input("Enter m n: ")).split(" ")
    ans = divide_3or7(m, n)
    print(ans)
    main()


if __name__=="__main__":
    main()