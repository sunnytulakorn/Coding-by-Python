#630510582
#tulakorn sawangmuang
#Section-001
#Lab10_1

import string 
def is_anagram(str1, str2): 
    answer1 = '' # Keep str1 in string
    answer2 = '' # keep str2 in stirng
    for i in str1: # run str1 letters
        if i in string.ascii_letters : # if str1 is letters
            answer1 += i # add the word in first string 

    for j in str2: # run str2 letters
        if j in string.ascii_letters : # if str2 is letters
            answer2 += j # add the word in second string

    x = answer1.lower() # change all letters to lower 
    y = answer2.lower() # change all letters to lower

    a = ''.join(sorted(x)) # sort and bring together letters 
    b = ''.join(sorted(y)) # sort and bring together letters 

    if a == b : # if str is all same
        return True
    else: # another condition 
        return False

def main():
    str1 = input("") # input letters
    str2 = input("") # input letters
    print(is_anagram(str1, str2)) # display answer
    main()

if __name__ == "__main__":
    main()