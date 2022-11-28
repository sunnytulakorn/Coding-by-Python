#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab08_2

def avg_number_row(list_x):
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
    list_x =  [['Python', -23, 40, 500], 
['Python', -23, 40, 500, 45, 33.45, 65545, 'az', 1.1, 'za']]
    list_result = avg_number_row(list_x)
    list_ans = []
    for i in list_result:
        x = "%.2f"%(i)
        x = float(x)
        list_ans.append(x)
    print(list_ans)

if __name__=="__main__":
    main()