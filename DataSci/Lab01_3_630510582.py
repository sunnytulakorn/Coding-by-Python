#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab01_3

def fncal_bmi(w, h):
    pound_to_kilo = w/2.2 #covert pounds to kilograms
    ft_to_cm = h*30.48 #covert feet to cm
    cm_to_m = ft_to_cm/100 #covert cm to m
    BMI_ = pound_to_kilo/(cm_to_m)**2 # BMI equation
    print("%.2f"%(BMI_))

def main():
    w = float(input())
    h = float(input())
    fncal_bmi(w, h)
    main() # recursive main

if __name__ == "__main__":
    main()