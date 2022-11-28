#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab09_1
import copy
from multiprocessing.sharedctypes import Value
def upd_student(stu_list, stu_id, new_weight):
    dict_stu = {}
    for i in stu_list:
        key = i[0]
        Value = i[1:]
        dict_stu[key] = Value

    dict_stuold = copy.deepcopy(dict_stu) 
    if stu_id in dict_stu:
        dict_stu[stu_id][2] = new_weight
    else:
        new_data = ['', 0, new_weight]
        dict_stu[stu_id] = new_data

    return(dict_stuold,dict_stu)

def main():
    stu_list =  [['6101001', 'Female', 1.38, 50.9],
['6102002', 'Male', 1.48, 60.2],
['6204222', 'Male', 1.55, 45.75]]
    stu_id = '6204111'
    new_weight = 50.5
    ans = (upd_student(stu_list, stu_id, new_weight))
    for i in range(len(ans)):
        print(ans[i])

if __name__=="__main__":
    main()