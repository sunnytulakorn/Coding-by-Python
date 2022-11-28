#630510582
#tulakorn sawangmuang
#Section-001
#Lab04-03
#evolution pidgey

import math

def calculate_p2p_evolve_exp(p, c):
    if p*12 == c: #condition
        pidgeotto = c//12 #Equation of pidgeotto
        exp = pidgeotto*500 #Equation of exp
    else: #Other
        c = (p-1) + c #Equation 
        pidgeotto = c//12 #Equation of pidgeotto
        if pidgeotto>p : #condition
            exp = p*500 #Equation of exp
        else: #Other
            exp = pidgeotto*500 #Equation of exp
    return exp #retrun this value to this function

def main():
    pidgey = int(input("")) # get number from user input
    candy = int(input("")) # get number from user input
    exp = calculate_p2p_evolve_exp(pidgey, candy) #Equation answer
    print("{0}".format(exp)) #answer

if __name__ == "__main__":
    main()
