#630510582
#tulakorn sawangmuang
#Section-001
#Lab10_3

def nondest_rotate_list(list_a, n):
    x = len(list_a) # define len list_a
    if n % len(list_a) == 0: # condition if display is same
        return list_a # the same value
    else: # another condition
        a = list_a[x - n%x:] # back half
        b = list_a[:x - n%x] # front half
        return (a + b) # display
    
def main():
    list_a = [1, 2, 3, 4] # define the value to cheak this function
    n = 105 # define number of the round to rotate
    print(nondest_rotate_list(list_a, n)) # display answer

if __name__ == "__main__":
    main()
