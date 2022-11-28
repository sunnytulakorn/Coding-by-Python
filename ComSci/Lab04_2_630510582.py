#630510582
#tulakorn sawangmuang
#Section-001
#Lab04-02
#Value display max mid min

def my_max_mid_min(a,b,c):
    if a>=b>=c or a>=c>=b: #Equation if a is max
        max = a #max
    elif b>=a>=c or b>=c>=a: #Equation if b is max
        max = b #max
    elif c>=a>=b or c>=b>=a: #Equation if c is max
        max = c #max
    if a>=b>=c or c>=b>=a: #Equation if b is mid
        mid = b #mid 
    elif a>=c>=b or b>=c>=a: #Equation if c is mid
        mid = c #mid
    elif c>=a>=b or b>=a>=c: #Equation if a is mid
        mid = a #mid
    if  a>=b>=c or b>=a>=c: #Equation if c is min
        min = c #min
    elif c>=b>=a or b>=c>=a: #Equation if a is min
        min = a #min
    elif c>=a>=b or a>=c>=b: #Equation if b is min
        min = b #min
    return print('max = {0} \nmid = {1} \nmin = {2}'.format(max,mid,min)) #display a max, mid, min value to return this function
    
def main():
    first = int(input(": ")) #get number from user input
    second = int(input(": ")) #get number from user input
    third = int(input(": ")) #get number from user input
    answer = my_max_mid_min(first,second,third) #Equation answer
    print('{0}'.format(answer)) #Answer

if __name__ == '__main__':
    main()
    


