#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab06_2

import string

def create_new_string(n, my_str):
    len_old_str = len(my_str)
    com_c = my_str.count(',')
    my_str_ct = com_c + 1

    if(my_str_ct < n):
        temp_str = "meaw meaw cat song".upper()
        m = 0
        for k in range(my_str_ct,n):
            new_str= temp_str[m:m+2] 
            my_str = my_str + "," + new_str 
            m = m + 2
 
    elif (my_str_ct > n):
        ans = ''
        bre = my_str_ct - n
        st = 0
        for i in my_str:
            if i == ',':
                if st < bre:
                    i.replace(",","")
                    st += 1
                else :
                    ans += i
            else:
                ans += i
        my_str = ans.upper()

    else: 
        my_str = my_str[::-1]
        my_str = my_str.lower()
 
    len_new_str = len(my_str)
 
    return len_old_str,my_str,len_new_str




def main():
    n = int(input("Enter n: ")) #รับข้อมูลน าเข้า
    str_ = input("Enter str: ")
    str_ = create_new_string(n, str_)
    print (str_[0])
    print (str_[1])
    print (str_[2])


if __name__=="__main__":
    main()