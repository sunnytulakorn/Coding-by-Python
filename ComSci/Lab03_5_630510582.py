#630510582
#tulakorn sawangmuang
#Section-001
#Lab03-05
#Change k of number to value

def kth_digit(number,k):
     number = (abs(number)%10**(abs(k)+1))//(10**abs(k)) #Equation of number
     return number #return number value to this function

def set_kth_digit(number,k,value):
    n = kth_digit(number,k) #Call n from function kth_digit(number,k)
    num = (abs(number)-(n*(10**k)))+(value*(10**k)) #Equation of num
    return num #return num value to this function

def main():
    number = int(input("")) #get number from user input
    k = int(input("")) #get k from user input
    value = int(input("")) #get value from user input
    num = set_kth_digit(number,k,value) #display num
    print("{0}".format(num)) #Answer

if __name__ == "__main__":
    main()