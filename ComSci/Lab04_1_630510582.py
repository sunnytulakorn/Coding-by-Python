#630510582
#tulakorn sawangmuang
#Section-001
#Lab04-01
#love6 function

def love6(first,second):
    if first == 6 or second == 6: #Equation if 1st or 2nd is 6
        return True #return answer value to this function
    elif first+second == 6: #Equation if 1st+2nd is 6
        return True #return answer value to this function
    elif abs(first-second) == 6: #Equation if abs(1st-2nd) is 6
        return True #return answer value to this function
    else: #Other
        return False #return answer value to this function

def main():
    first = int(input(": ")) #get number from user input
    second = int(input(": ")) #get number from user input
    answer = love6(first,second) #display answer
    print('{0}'.format(answer)) #Answer

if __name__ == "__main__":
    main()