#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab02_2

def draw_square(n, ch1, ch2):
    half = n//2
    double = 2*n
    show_sharp_star(ch1, ch2, double-half, half)
    show_sharp_star(ch1, ch2, n, n)
    show_sharp_star(ch1, ch2, 0, double)
    show_sharp_star(ch1, ch2, n, n)
    show_sharp_star(ch1, ch2, double-half, half)


def show_sharp_star(ch1, ch2, i, j):
    print(ch1*i+ch2*j)

def main():
    n = int(input())
    ch1 = input()
    ch2 = input()
    draw_square(n, ch1, ch2)
    main()

if __name__=="__main__":
    main()