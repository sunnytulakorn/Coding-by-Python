#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab09_4

def bmi_reports(stu_list):
    ans = {'Normal' : [],'Over' : [],'Under' : [],'Obesity' : []}
    Level_ = ["Over","Normal","Under","Obesity"]
    for i in stu_list:
        bmi = (i[3]/((i[2])**2))
        bmi = round(bmi, 1)
        if  25<= bmi < 30 :
            ans['Over'].append([i[0], bmi])
        elif 18.5<= bmi < 25:
            ans['Normal'].append([i[0], bmi])
        elif bmi < 18.5:
            ans['Under'].append([i[0], bmi])
        elif bmi >= 30:
            ans['Obesity'].append([i[0], bmi])
    for i in Level_:
        if ans[i] == []:
            ans.pop(i)
    return ans
    

def main():
    stu_list = [['6101001', 'Female', 1.38, 50.9],['6102002', 'Male', 1.48, 60.2],['6204222', 'Male', 1.55, 45.75]]
    result = bmi_reports(stu_list)
    print(result)

if __name__=="__main__":
    main()