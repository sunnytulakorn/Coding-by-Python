#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab06_1
import string

def replace_string(str_input):
    check = "AEIOU1234567890"
    replace="@#$&*0000000000"
    vowels = check
 
    for i in range(len(vowels)):
        str_input = str_input.upper()
        str_input = str_input.replace(check[i], replace[i])

    return str_input

def main():
    str_input = input("Enter str: ") 
    new_str = replace_string(str_input)
    print(new_str)

if __name__=="__main__":
    main()