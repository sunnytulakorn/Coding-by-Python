#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab06_3

def replace_string(str_input, str_check, str_replace):
    for i in range(len(str_check)):
        str_input = str_input.replace(str_check[i], str_replace[i])

    return str_input

def main():
    str_input = input("Enter str: ") 
    str_check = input()
    str_replace = input()
    ans = replace_string(str_input, str_check, str_replace)
    print(ans)

if __name__=="__main__":
    main()