def multiple_mn(m,n):
    first_last = []
    middle = []
    all_list = []
    for i in range(0,n):
        first_last.append(1)
        if i == 0:
            middle.append(1)
        elif i == n-1:
            middle.append(1)
        else:
            middle.append(0)

    for i in range(0, m):
        if i == 0:
            all_list.append(first_last)
        elif i == m-1:
            all_list.append(first_last)
        else:
            all_list.append(middle)
    
    return all_list
    
def main():
    m = int(input())
    n = int(input())
    print(multiple_mn(m,n))

if __name__=="__main__":
    main()