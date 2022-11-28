#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab09_2

def grp_reports(stu_list):
    genderList = {"Female" : [], "Male" : []}
    major_ = {"01": None,"02": None,"03": None,"04": None,"05":None}
    majorList_ = ["01","02","03","04","05"]
    room=[[],[],[],[],[]]
    for i in range (len(stu_list)):
        if(stu_list[i][1] == "Female"):
            genderList['Female'].append(stu_list[i][0])
        else:
            genderList['Male'].append(stu_list[i][0])
        stuRoom = stu_list[i][0]
        if(str(stuRoom[2:4]) == "01"):
            room[0].append(stu_list[i][0])
        elif(str(stuRoom[2:4]) == "02"):
            room[1].append(stu_list[i][0])
        elif(str(stuRoom[2:4]) == "03"):
            room[2].append(stu_list[i][0])
        elif(str(stuRoom[2:4]) == "04"):
            room[3].append(stu_list[i][0])
        elif(str(stuRoom[2:4]) == "05"):
            room[4].append(stu_list[i][0])
    num = 0
    for i in majorList_:      
        major_[i] = tuple(room[num])
        num+=1
    return(genderList,major_)

def main():
    stu_list =  [['6101001', 'Female', 1.38, 50.9],
['6102002', 'Male', 1.48, 60.2],
['6204222', 'Male', 1.55, 45.75],
['6305100', 'Female', 1.65, 63.2],
['6403111', 'Male', 1.53, 44.5],
['6401127', 'Male', 1.47, 49.8]]

    ans = grp_reports(stu_list) 
    print(ans)

if __name__=="__main__":
    main()