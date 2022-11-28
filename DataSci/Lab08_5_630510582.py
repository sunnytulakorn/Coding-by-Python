#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab08_5

def  pretty_print_list(list_a):
    rows = len(list_a)
    cols = len(list_a[0])
    length_list = []
    for row in range(rows):
        for col in range(cols):
            length_list.append(len(str(list_a[row][col])))
    
    max_length = max(length_list)

    max_l = "{0:>" + str(max_length) + "}"

    print("[", end='')
    for row in range(rows):
        if row == 0:
            print("[", end='')
        else:
            print(" [", end='')
        for col in range(cols):
            if col < cols-1:
                print(max_l.format(list_a[row][col]),end=',')
            else:
                print(max_l.format(list_a[row][col]),end='')
        if row == rows-1:
            print("]", end='')
        else:
            print("],")
    print("]")

def main():
    list_a =  [[134, 2, 3], [4, 75, 6],[122, 3, 1233331234]]  
    pretty_print_list(list_a)

if __name__=="__main__":
    main()