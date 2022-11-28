#630510582
#tulakorn sawangmuang
#section-001
#Lab03-02
#reverse number
def reverse_digits(x):
    x = ((abs(x)%10)*1000)+(((abs(x)%100)//10)*100)+(((abs(x)%1000)//100)*10)+(abs(x)//1000) #Equation of x
    return x #return x value to this function
def main():
    x = int(input("Input: ")) #get x from user input
    output = reverse_digits(x) #display output
    print("output:{0}".format(output)) #Answer
if __name__=='__main__':
    main()

