#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab07_5

def replace_sorting(list_input, item):
    list_x = []
    list_0 = []
    for i in list_input:
        if i != item:
            list_x.append(i)
        else:
            list_0.append(0)

    ans = list_0 + list_x
    ans.sort()
    return ans

def main():
    list_input = [45, 3, 8, 3 , 42]
    item = int(input("Enter item: "))
    print(replace_sorting(list_input, item))

if __name__=="__main__":
    main()