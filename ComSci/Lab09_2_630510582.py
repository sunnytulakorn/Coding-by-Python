#630510582
#tulakorn sawangmuang
#Section-001
#Lab09_2
def n_base_to_10(n, num):
    if num == 0: # base case
        return 0
    else: # call n_base_to_10 function 
        return n*(n_base_to_10(n, num//10)) + num%10 # equation function to run 


def main():
    n = int(input()) # input n
    num = int(input()) # input num
    print(n_base_to_10(n, num)) # display 
    main()

if __name__ == "__main__":
    main()