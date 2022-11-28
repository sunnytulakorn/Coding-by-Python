#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab03_2

def wavelength(w):
    if 380 <= w < 450 :
        return "Violet"
    elif 450 <= w < 495 :
        return "Blue"
    elif 495 <= w < 570 :
        return "Green"
    elif 570 <= w < 590 :
        return "Yellow"
    elif 590 <= w < 620 :
        return "Orange"
    elif 620 <= w < 750 :
        return "Red"
    else:
        return "Invalid Input"

def main():
    w = int(input())
    ans = wavelength(w)
    print(ans)
    main()

if __name__=="__main__":
    main()