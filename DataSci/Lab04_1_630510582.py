#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab04_1

def sequence_number(n):
    for i in range(n):
        print(2*i+1,end=" ")

def main():
    n = int(input())
    sequence_number(n)

if __name__=="__main__":
    main()