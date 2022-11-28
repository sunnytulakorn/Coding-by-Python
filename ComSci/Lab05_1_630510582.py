#630510582
#tulakorn sawangmuang
#Section-001
#Lab05-01
#intersects

def intersects(x1,y1,r1,x2,y2,r2, epsilon=10**-6):
    d = (((x2-x1)**2 + (y2-y1)**2)**0.5) #Equation of d

    if d > r1 and d > r2 : #condition
        if abs(d - (r1+r2)) <= epsilon : #condition
            result = 0  #value
        elif d < r1 + r2 : #another condition
            result = 1 #value
        else: #other condition
            result = -1 #value
    else: #other condition
        if r1 > r2 : #condition
            r_max = r1 #value
            r_min = r2 #value
        else: #other condition
            r_max = r2 #value
            r_min = r1 #value
        if abs(r_max - r_min - d) <= epsilon : #condition
            result = 0 #value
        elif r_max - r_min - d < 0 : #another condition
            result = 1 #value
        else: #other condition
            result = -1 #value
    return result #return this value to this function

def main():
    x1 = float(input()) # get number from user input
    y1 = float(input()) # get number from user input
    r1 = float(input()) # get number from user input
    x2 = float(input()) # get number from user input
    y2 = float(input()) # get number from user input
    r2 = float(input()) # get number from user input
    print(intersects(x1,y1,r1,x2,y2,r2, epsilon=10**-6)) #answer

if __name__ == '__main__':
    main()