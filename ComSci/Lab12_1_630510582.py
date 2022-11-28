#630510582
#tulakorn sawangmuang
#Section-001
#Lab12_1
import copy
import string
def sort_date(list_x):
    x = copy.deepcopy(list_x)
    ans = []
    strr = ''
    for i in x:
        a = str(i)
        for j in a:
            if j not in string.punctuation:
                strr += j
                


        
    print(ans)


def main():
    list_x = ["11/1/2100", "5/12/1999", "19/1/2003", "11/9/2001"]
    sort_date(list_x)
    print("---")
    print(list_x)

if __name__ == "__main__":
    main()
