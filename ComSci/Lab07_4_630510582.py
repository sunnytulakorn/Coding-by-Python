#630510582
#tulakorn sawangmuang
#Section-001
#Lab07_4

def life_path(n):
    n != 0 # condition
    result = 0 # result value
    answer = 0 # answer value
    real_answer = 0 # real value
    while n > 0: #condition to do this loop
        a = n%10 #equation a
        result += a # plus a to result
        n = n//10 # next number

    if result > 0: # condition
        while result > 0: # condition to do this loop
            b = result%10 # equation b
            answer += b # plus b value to answer
            result = result//10 # if 2 digit number do it agian in lower condition

    if answer != 0: # condition
        while answer > 0: # condition to do this loop
            c = answer%10 # equation c
            real_answer += c # plus c in real answer
            answer = answer//10 # next number

    return real_answer # display value

def main():
    n = int(input()) # input the value
    print(life_path(n)) #display value

if __name__ == "__main__":
    main()



