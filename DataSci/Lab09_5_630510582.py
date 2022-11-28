#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab09_5

def grp_search(stu_list, gender, year):
    genderdict = {'Female' : [],'Male' : []}
    y_Dict = {'61' : [],'62' : [],'63' : [],'64' : [],'65' : []}
    year_List = {"61","62","63","64","65"}
    genderlist = set()
    
    for i in stu_list:
        if i[1] == 'Female':
            genderdict['Female'].append(i[0])
        elif i[1] == 'Male':
            genderdict['Male'].append(i[0])

    for i in stu_list:
        word = i[0]
        if word[0:2] == '61':
            y_Dict['61'].append(i[0])
        elif word[0:2] == '62':
            y_Dict['62'].append(i[0])
        elif word[0:2] == '63':
            y_Dict['63'].append(i[0])
        elif word[0:2] == '64':
            y_Dict['64'].append(i[0])
        elif word[0:2] == '65':
            y_Dict['65'].append(i[0])
            
    for i in year_List:
        if y_Dict[i] == []:
            y_Dict.pop(i)
    if gender == 'Female':
        for i in genderdict['Female']:
            genderlist.add(i)
    else:
        for i in genderdict['Male']:
            genderlist.add(i)

    for i in stu_list:
        word = i[0]
        if word[0:2] == year:
            genderlist.add(i[0])
    genderlist = list(genderlist)
    genderlist.sort()

    return genderdict, y_Dict, genderlist

def main():
    stu_list = [['6101001', 'Female', 1.38, 50.9],['6102002', 'Male', 1.48, 60.2],['6204222', 'Male', 1.55, 45.75],['6305100', 'Female', 1.65, 63.2],['6403111', 'Male', 1.53, 44.5],['6401127', 'Male', 1.47, 49.8]]
    gender = 'Female'
    year = '61'
    result = grp_search(stu_list, gender, year)
    print(result[0])
    print(result[1])
    print(result[2])

if __name__=="__main__":
    main()