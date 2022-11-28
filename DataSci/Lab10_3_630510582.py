#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab10_3

def find_avg_number(list_x):
    list_sum = []
    list_plus = []
    row = len(list_x)
    count = 0
    for i in range(row):
        for j in range(len(list_x[i])):
            if isinstance(list_x[i][j], int):
                list_plus.append(list_x[i][j])
                count += 1
            if isinstance(list_x[i][j], float):
                list_plus.append(list_x[i][j])
                count += 1
        Sum_ = (sum(list_plus)/count)
        list_sum.append(Sum_)
        list_plus = []
        count = 0
    
    return list_sum

def main():
    list_x = input()
    print(find_avg_number)

if __name__=="__main__":
    main()
