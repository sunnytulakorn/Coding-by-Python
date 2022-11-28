#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab03_4

def cal_bmi(w, h):
    height_cm_inch = h*30.48
    cm_to_m = h / 100
    ft_to_inch = h * 12
    if (height_cm_inch < 300):
        bmi = ((w/(ft_to_inch**2))*703)
    else:
        bmi = (w/(cm_to_m**2))

    print("%.1f"%(bmi))

def main():
    weight = float(input())
    height = float(input())
    cal_bmi(weight, height)
    main()

if __name__=="__main__":
    main()
