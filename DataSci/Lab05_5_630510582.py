#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab05_5

def triangle_tree(n):
    for i in range(n+1):
        for k in range(1, i+1):
            show_space_star(n-k,k*2-1)
            

def show_space_star(i, j):
    print(" "*i, end='')
    print(" "*i,"* "*j,end="\n")


def main():
    n = int(input("Enter star number: "))
    triangle_tree(n)

if __name__=="__main__":
    main()