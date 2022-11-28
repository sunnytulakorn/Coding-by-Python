#630510582
#tulakorn sawangmuang
#Section-001
#Lab10_2

def classify(list_x):
    list_a = [] #int list
    list_b = [] #float list
    list_c = [] #string list
    for i in list_x : # loop to run the list
        if  isinstance(i, int): #check int
            list_a += [i] # add this value to int list
        if  isinstance(i, float): #check float
            list_b += [i] # add this value to float list
        if isinstance(i, str): #check string
            list_c += [i] # add this value to string list
    return (list_a, list_b ,list_c) # display

def main():
    list_x = [10, 'hello', 23.5, 4] # define value to cheak this function
    print(classify(list_x)) # display answer 

if __name__ == "__main__":
    main()


    
