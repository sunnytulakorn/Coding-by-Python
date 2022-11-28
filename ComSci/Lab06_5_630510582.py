#630510582
#tulakorn sawangmuang
#Section-001
#Lab06_5

def longest_digit_run(n):
    n != 0 # define n not 0
    numbers = 1 # Duplicate numbers
    result = 0 # amount duplicate numbers
    while n > 0: # do loop when n>0
        a = n % 10 # equation
        b = (n % 100)//10 # equation
        if a == b: # condition
            numbers += 1 # have a Duplicate numbers
        else: # other
            numbers = 1 # return numbers to 1
        n = n//10 # Move to next number to find a duplicate numbers
        if numbers >= result: # condition to plus result
            result = numbers # value
    
    return result # return answer

def main():
    n = int(input()) # input the number
    answer = longest_digit_run(n) # equation answer
    print("{0}".format(answer)) # show the answer

if __name__ == "__main__":
    main()