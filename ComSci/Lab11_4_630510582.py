#630510582
#tulakorn sawangmuang
#Section-001
#Lab11_4
import copy
def sum_nested_list(list_a):
    co = copy.deepcopy(list_a) # copy list_a
    for i in co :
        if isinstance(i, list): # check list
            while isinstance(i, list): # check list agian
                co.extend(i) # plus value
                break # stop 
            continue # do agian
    for j in range(len(co)): # run value
        if isinstance(co[j], list): # if it list
            co[j] = 0 # list = 0(int)
    return sum(co) # sum

def main():
    list_a = [1, 2, [[2, [[145], 34]], [48, 22]]]
    print(sum_nested_list(list_a))

if __name__ == "__main__":
    main()




