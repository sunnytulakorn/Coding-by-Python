#630510582
#tulakorn sawangmuang
#Section-001
#Lab05-03
#songkran day

def count_down_to_songkran(d, m, y):
    fe1 = feb1(y) #Equation
    fe2 = feb2(y) #Equation
    if d > 0: #condition
        if m == 1: #condition
            return (75+fe1)-d #return this value to this function
        elif m == 2: #another condition
            return (fe1+44)-d #return this value to this function
        elif m == 3: #another condition
            return 44-d #return this value to this function
        elif m == 4: #another condition
            if d <= 13: #condition
                return 13-d #return this value to this function
            else: #other condition
                return (30-d)+245+(75+fe2) #return this value to this function
        elif m == 5: #another condition
            return (31-d)+214+(75+fe2) #return this value to this function
        elif m == 6: #another condition
            return (30-d)+184+(75+fe2) #return this value to this function
        elif m == 7: #another condition
            return (31-d)+153+(75+fe2) #return this value to this function
        elif m == 8: #another condition
            return (31-d)+122+(75+fe2) #return this value to this function
        elif m == 9: #another condition
            return (30-d)+92+(75+fe2) #return this value to this function
        elif m == 10: #another condition
            return (31-d)+61+(75+fe2) #return this value to this function
        elif m == 11: #another condition
            return (30-d)+31+(75+fe2) #return this value to this function
        elif m == 12: #another condition
            return (31-d)+(75+fe2) #return this value to this function

def feb1(y):
    if y / 4 == int(y / 4) : #condition
        if y % 100 == 0 : #condition
            if y % 400 == 0: #condition
                return 29 #return this value to this function
            else: #other condition
                return 28 #return this value to this function
        else: #other condition
            return 29 #return this value to this function
    else: #other condition
        return 28 #return this value to this function    
            
def feb2(y):
    if (y+1) / 4 == int((y+1) / 4) : #condition
        if (y+1) % 100 == 0 : #condition
            if (y+1) % 400 == 0: #condition
                return 29 #return this value to this function
            else: #other condition
                return 28 #return this value to this function
        else: #other condition
            return 29 #return this value to this function
    else: #other condition
        return 28 #return this value to this function

def main():
    d = int(input("")) # get number from user input
    m = int(input("")) # get number from user input
    y = int(input("")) # get number from user input
    print(count_down_to_songkran(d, m, y)) #answer    
            
if __name__== '__main__':
    main()