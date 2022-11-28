#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab04_2

def reverse_sequence_number(m,n):
    m = int(m)
    n = int(n)
    for i in range(m, n-1, -2):
        print(i, end=" ")

def main():
    m, n = (input("Enter m,n: ")).split(",")
    reverse_sequence_number(m,n)
if __name__=="__main__":
    main()