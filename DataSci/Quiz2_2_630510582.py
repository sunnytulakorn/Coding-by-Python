import copy

def pair_request(list_input, sum):
    copy_list = copy.deepcopy(list_input)
    list_ans = []
    for i in list_input:
        copy_list.pop(0)
        for j in copy_list:
            if i+j == sum:
                list_ans.append([i,j])
                 
    return list_ans

def main():
    list_input = [1, 9, 5, 7, 10, 3]
    sum_ = int(input())
    print(pair_request(list_input, sum_))
    main()

if __name__=="__main__":
    main()