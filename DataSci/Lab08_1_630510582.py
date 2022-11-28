#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab08_1

def classify_lists_result(list_x):
    list_a = []
    list_b = []
    list_c = []

    for i in list_x:
        if isinstance(i, int):
            list_a.append(i)
        elif isinstance(i,float):
            list_b.append(i)
        elif isinstance(i, str):
            list_c.append(i)

    sum_a = sum(list_a)
    avg_b = sum(list_b)/len(list_b)
    # str_c = sorted(list_c, key=str.casefold)
    list_c.sort(key=lambda x: x.lower())

    return sum_a,avg_b,list_c


def main():
    list_x = ['Python', -23, 40, 500,45,33.45,65545,'az',1.1,'za']
    list_result = classify_lists_result(list_x)
    print(list_result[0])
    print("%.3f"%(list_result[1]))
    print(list_result[2])

if __name__=="__main__":
    main()