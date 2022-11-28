#630510582
#tulakorn sawangmuang
#Section-001
#Lab03-04
#Restore k to number

def kth_digit(number,k):
     number = (abs(number)%10**(abs(k)+1))//(10**abs(k)) #Equation of number
     return number #return number value to this function

def main():
    number = int(input("")) #get number from user input
    k = int(input("")) #get k from user input
    output = kth_digit(number,k) #display output
    print('{0}'.format(output)) #Answer

if __name__ =='__main__':
    main()
