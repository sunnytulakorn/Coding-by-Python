#630510582
#tulakorn sawangmuang
#Section-001
#Lab05-05
#Chinese zodiac

def zodiac_element(year):
    if year%12 == 0: #condition
        x = "Monkey" #display
    elif year%12 == 1: #another condition
        x = "Rooster" #display
    elif year%12 == 2: #another condition
        x = "Dog" #display
    elif year%12 == 3: #another condition
        x = "Pig" #display
    elif year%12 == 4: #another condition
        x = "Rat" #display
    elif year%12 == 5: #another condition
        x = "Ox" #display
    elif year%12 == 6: #another condition
        x = "Tiger" #display
    elif year%12 == 7: #another condition
        x = "Rabbit" #display
    elif year%12 == 8: #another condition
        x = "Dragon" #display
    elif year%12 == 9: #another condition
        x = "Snake" #display
    elif year%12 == 10: #another condition
        x = "Horse" #display
    elif year%12 == 11: #another condition
        x = "Goat" #display
    if year%10 == 0 or year%10 == 1: #condition
        y = "Metal" #display
    elif year%10 == 2 or year%10 == 3: #another condition
        y = "Water" #display
    elif year%10 == 4 or year%10 == 5: #another condition
        y = "Wood" #display
    elif year%10 == 6 or year%10 == 7: #another condition
        y = "Fire" #display
    elif year%10 == 8 or year%10 == 9: #another condition
        y = "Earth" #display
    return ("{0} {1}".format(y,x)) #return this value to this function

def main():
    year = int(input("")) # get number from user input
    answer1 = zodiac_element(year) #display answer equation
    print("{0}".format(answer1)) #answer

if __name__ == "__main__":
    main()
    


    
