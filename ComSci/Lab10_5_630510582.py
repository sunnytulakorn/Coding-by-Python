#630510582
#tulakorn sawangmuang
#Section-001
#Lab10_5

def three_digits_to_word(n):
    answer = "" # kepp value
    digit = ["","one","two","three","four","five","six","seven","eight","nine",] # list digits
    Ten_twenty = ["ten","eleven","twelve","thirteen","fourteen","fifteen", "sixteen", "seventeen","eighteen","nineteen"] # 10-19 value
    Tens_digit = ["","","twenty","thirty", "forty","fifty","sixty", "seventy", "eighty", "ninety",""] # more than 19 value but not over 100
    x,y = divmod(n,100) # find divide and mod 
    if x == 0: # condition
        y,z = divmod(n,10) # find divide and mod 
        if y == 0: # condition 
            answer = "".join(digit[z]) # combine the list
        else: # another conditions
            if y == 1: # condition
                answer = "".join(Ten_twenty[n%10]) # more than 19 value
            else: # another 
                if z > 0: # condition
                    answer = "".join(Tens_digit[y])+"-"+"".join(digit[z]) # combine 
                else:
                    answer = "".join(Tens_digit[y])+"".join(digit[z]) # conbine
    else: # another condition
        answer = "".join(digit[x]) + " hundred " # if it more than 100 value
        n %= 100 
        y,z = divmod(n,10) # find divide and mod
        if y == 0: 
            answer += "".join(digit[z]) #combine
        else:
            if y == 1:
                answer += "".join(Ten_twenty[n%10])
            else:
                if z != 0:
                    answer += "".join(Tens_digit[y]) + "-" + "".join(digit[z]) # combine answer
                else:
                    answer += "".join(Tens_digit[y]) + "".join(digit[z]) # combine answer
    return answer # display value
    
    
def num_to_word(num): # find the num to word 
    if num == 0: 
        return "zero" # if the value is 0
    n = [] # collector in type list
    s = "" # collector in type string
    while num > 0 or num < 0 : # loop to rn this value
        n.append(num%1000) # add on the back 
        num //= 1000 # run value
    n.reverse() # rotate value

    bil_mil_lion = ["billion","million","thousand",""] # if is more than 1 million
    z = 0 

    if len(n) == 1:
        s += "".join(three_digits_to_word(n[0]))
    if len(n) == 2:
        for i in n:
            if i != 0:
                s += "".join(three_digits_to_word(n[z]))
                s += " "
                s += "".join(bil_mil_lion[z+2])
                if n[1] > 0:
                    s += " "
                z += 1
    if len(n) == 3:
        z = 3
        for i in n:
            if i != 0:
                s += "".join(three_digits_to_word(n[z-3]))
                s += " "
                s += "".join(bil_mil_lion[z-2])
                if n[z-(z-1)] > 0:
                    s += " "
                z += 1
    if len(n) == 4:
        z = 0
        for i in n:
            if i != 0:
                s += "".join(three_digits_to_word(n[z]))
                s += " "
                s += "".join(bil_mil_lion[z])
                s += " "
                z += 1
        s = s[:-1]
    return s


def main():
    num = int(input())
    print(num_to_word(num))
    main()

if __name__ == "__main__":
    main()