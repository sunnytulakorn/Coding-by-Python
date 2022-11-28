#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab07_3

def list_number(n):
    ans = 0
    list_x = []
    for i in range(n):
        ans = 2*i+1
        list_x.append(ans)
        ans = 0
    
    return list_x

def main():
    n = int(input("Enter n: "))
    n_result = list_number(n)
    for i in n_result:
        print(i, end=" ")


if __name__=="__main__":
    main()

