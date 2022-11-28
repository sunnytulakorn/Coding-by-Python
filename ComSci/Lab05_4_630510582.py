#630510582
#tulakorn sawangmuang
#Section-001
#Lab05-04
#overlapped

def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):
    if (l1+w1) < l2 or (l2+w2) < l1: #condition
        return False #display
    elif (t1+h1) < t2 or (t2+h2) < t1: #another condition
        return False #display
    else: #other condition
        return True #display

def main():
    l1 = int(input("")) # get number from user input
    t1 = int(input("")) # get number from user input
    w1 = int(input("")) # get number from user input
    h1 = int(input("")) # get number from user input
    l2 = int(input("")) # get number from user input
    t2 = int(input("")) # get number from user input
    w2 = int(input("")) # get number from user input
    h2 = int(input("")) # get number from user input
    answer = is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2) #display answer equation
    print("{0}".format(answer)) #answer

if __name__ == "__main__":
    main()



