#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab09_3

def counting_reports(stu_list):
    keep1 = {'Female': 0,'Male' : 0}
    keep2 = {'01' : 0,'02' : 0,'03' : 0,'04' : 0,'05' : 0}
    keep3 = {4 : 0,3 : 0,2 : 0,1 : 0}
    year_List = [4,3,2,1]
    for i in stu_list:
        if i[1] == 'Female':
            keep1['Female'] += 1
        else:
            keep1['Male'] += 1
    for i in stu_list:
        word = i[0]
        if word[2:4] == '01':
            keep2['01'] += 1
        elif word[2:4] == '02':
            keep2['02'] += 1
        elif word[2:4] == '03':
            keep2['03'] += 1
        elif word[2:4] == '04':
            keep2['04'] += 1
        elif word[2:4] == '05':
            keep2['05'] += 1
    for i in stu_list:
        word = i[0]
        if int(word[1]) == 1:
            keep3[4] += 1
        elif int(word[1]) == 2:
            keep3[3] += 1
        elif int(word[1]) == 3:
            keep3[2] += 1
        elif int(word[1]) == 4:
            keep3[1] += 1
    for i in year_List:
        if keep3[i] == 0:
            keep3.pop(i)
    return keep1, keep2, keep3

def main():
    stu_list = [['6101022', 'Female', 1.68, 66.9],['6102127', 'Male', 1.58, 50.2],['6104222', 'Male', 1.61, 60.1],['6105533', 'Female', 1.51, 53.2],['6105711', 'Male', 1.35, 40.5],['6301127', 'Male', 1.57, 50.8],['6301321', 'Male', 1.51, 60.1],['6303432', 'Female', 1.77, 53.2],['6405411', 'Male', 1.55, 45.5],['6405711', 'Male', 1.85, 60.5]]
    result = counting_reports(stu_list)
    print(result[0])
    print(result[1])
    print(result[2])
    

if __name__=="__main__":
    main()