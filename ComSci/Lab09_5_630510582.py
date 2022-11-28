#630510582
#tulakorn sawangmuang
#Section-001
#Lab09_5
import string
def reverse_num(num):
    if num < 10 : #base case
        return  num
    else:
        x = (num%10)*(10**(len(str(num))-1)) + reverse_num(num//10) # call function reverse_num
        return x # update and display number

def main():
    num = int(input()) # input value 
    print(reverse_num(num)) # display number
    main()
    


if __name__ == "__main__":
    main()