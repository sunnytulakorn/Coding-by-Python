#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab07_1

def classify_lists(list_x):
    list_a = []
    list_b = []
    list_c = []

    for i in list_x:
        if isinstance(i, int):
            list_a.append(i)
        if isinstance(i,float):
            list_b.append(i)
        if isinstance(i, str):
            list_c.append(i)

    return list_a,list_b,list_c

def main():
    list_x = [10, 'hello', 23.5, 4]
    list_result = classify_lists(list_x)
    print(list_result[0])
    print(list_result[1])
    print(list_result[2])

if __name__=="__main__":
    main()