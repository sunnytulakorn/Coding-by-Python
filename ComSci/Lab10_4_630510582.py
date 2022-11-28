#630510582
#tulakorn sawangmuang
#Section-001
#Lab10_4

def dest_rotate_list(list_a, n):
    x = len(list_a) # define len list_a
    if n % x == 0 : # conditon if it same value
        return list_a # the same value
    else:
        if n > 0 : # if n > 0
            for i in range(n): #loop to switch the list
                a = list_a.pop(-1) # delete last value
                list_a.insert(0, a) # add on front
        else: # another condition
            for i in range(abs(n)): # loop to switch the list
                b = list_a.pop(0) # delete front value
                list_a.append(b) # add on last 

def main():
    list_a = [1, 2, 3, 4] # define to cheak this function
    n = -1 # define round to rotate this list
    dest_rotate_list(list_a, n) # call function
    print(list_a) # display answer

if __name__ == "__main__":
    main()