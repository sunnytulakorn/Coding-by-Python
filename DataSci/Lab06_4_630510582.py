#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab06_4

import string

def new_string(name1, name2, name3, name4, name5):
    ans1 = name1[0:2]+'_'+name2[0:2]+'_'+name3[0:2]+'_'+name4[0:2]+'_'+name5[0:2]
    ans2 = name1[:-3:-1]+'/'+name2[:-3:-1]+'/'+name3[:-3:-1]+'/'+name4[:-3:-1]+'/'+name5[:-3:-1]
    ans3 = name1[0::len(name1)-1]+'*'+name2[0::len(name2)-1]+'*'+name3[0::len(name3)-1]+'*'+name4[0::len(name4)-1]+'*'+name5[0::len(name5)-1]
    return(ans1,ans2,ans3)

def main():
    name1, name2, name3, name4, name5 = input("Enter str: ").split(",")
    ans = (new_string(name1, name2, name3, name4, name5))
    print(ans[0])
    print(ans[1])
    print(ans[2])

if __name__=="__main__":
    main()