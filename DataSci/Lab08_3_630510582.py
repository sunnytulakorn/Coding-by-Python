#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab08_3
import copy

def remove_row_col(list_a, row, col):
    list_ans = copy.deepcopy(list_a)
    for i in list_ans:
        del i[col]
    
    del list_ans[row]
    return list_ans


def main():
    list_a = [[2, 3, 4, 5], [8, 7, 6, 5], [0, 1, 2, 3]]
    row = int(input())
    col = int(input())
    list_result = remove_row_col(list_a, row, col)
    print(list_result)

if __name__=="__main__":
    main()