#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab07_2

def sum_number(list_x):
    list_sum = []

    for i in list_x:
        if isinstance(i, int):
            list_sum.append(i)
        elif isinstance(i, float):
            list_sum.append(i)

    x = sum(list_sum)
    return x


def main():
    list_x = ['Python', -23.1, 40.2, 500]
    list_result = sum_number(list_x)
    print(list_result)

if __name__=="__main__":
    main()