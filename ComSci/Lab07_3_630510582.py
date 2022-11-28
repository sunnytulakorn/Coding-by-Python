#630510582
#tulakorn sawangmuang
#Section-001
#Lab07_3

def triangle(n):
    print('*') # print *
    for i in range(n-2): # loop
        print('*.'+i*'..'+'*') # print pic
    print(n*'* ') # display * under
    
def main():
    n = int(input()) # input row
    triangle(n) # display triangle pic
    main()
    
if __name__ == "__main__":
    main()
    
    
