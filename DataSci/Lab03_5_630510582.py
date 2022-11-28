#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab03_5

def cal_bmi(w, h):
    height_cm_inch = h*30.48
    cm_to_m = h / 100
    ft_to_inch = h * 12
    if (height_cm_inch < 300):
        bmi = ((w/(ft_to_inch**2))*703)
    else:
        bmi = (w/(cm_to_m**2))

    return(bmi)

def bmi_guide(bmi):
    print("%.1f"%(bmi))
    if bmi < 18.5:
        print("underweight")
    elif 18.5 <= bmi <= 22.99:
        print("normal")
    elif 23.0 <= bmi <= 24.99:
        print("overweight")
    elif 25.0 <= bmi <= 29.99:
        print("obese")
    else:
        print("severely obese")


def main():
    w = float(input())
    h = float(input())
    bmi = cal_bmi(w, h)
    bmi_guide(bmi)
    main()

if __name__=="__main__":
    main()
