#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab08_4

def multiple_list(n):
    run_ = 0
    if n > 12:
        return("Invalid Input")
    else:
        list_result = make_2d_list(n, n)
        for i in range(0,n):
            for j in range(0,n):
                run_ += 1
                result = run_*(i+1)
                list_result[i][j] = result
            run_ = 0
    return list_result

def make_2d_list(rows, cols):
    a = []
    for row in range(rows):
        a += [[0] * cols]
    return a

def main():
    n = int(input("Enter n: "))
    list_result = multiple_list(n)
    print(list_result)

if __name__=="__main__":
    main()