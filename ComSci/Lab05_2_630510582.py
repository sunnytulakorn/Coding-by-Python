#630510582
#tulakorn sawangmuang
#Section-001
#Lab05-02
#Pythagorean triple

import math

def is_p_triple(a, b, c):
    if a**2 + b**2 == c**2: #condition
        return True #display
    elif a**2 + c**2 == b**2: #another condition
        return True #display
    elif c**2 + b**2 == a**2: #another condition
        return True #display
    else: #other condition
        return False #display

def main():
    a = int(input()) # get number from user input
    b = int(input()) # get number from user input
    c = int(input()) # get number from user input
    answer = is_p_triple(a, b, c) #display answer equation
    print("{0}".format(answer)) #answer

if __name__ == "__main__":
    main()
