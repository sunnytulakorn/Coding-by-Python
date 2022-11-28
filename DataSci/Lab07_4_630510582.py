#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab07_4

def reverse_list_number(m,n):
    m = int(m)
    n = int(n)
    list_x = []
    for i in range(m, n-1, -2):
        list_x.append(i)

    return(list_x)


def main():
    m,n = input("Enter m,n: ").split(",")
    ans = reverse_list_number(m,n)
    for i in ans:
        print(i, end=" ")

if __name__=="__main__":
    main()