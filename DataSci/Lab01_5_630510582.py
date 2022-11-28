#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab01_5

def display_time(sec):
    day = sec//86400 #Equation day
    y = sec%86400 #Equation y
    hour = y//3600 #Equation hour
    z = y%3600 #Equation z
    minute = z//60 #Equation minute
    a = z%60 #Equation a
    second = a #Equation second
    print("%d:%.2d:%.2d:%.2d"%(day,hour,minute,second))

def main():
    sec = int(input())
    display_time(sec)
    main() # recursive main

if __name__ == "__main__":
    main()