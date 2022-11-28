#630510582
#tulakorn sawangmuang
#Section-001
#Lab08_1

def square_frame(n, sep=' '):
    x = [] # keep value
    a = n**2 - ((n-2)**2) # equation
    for i in range(1, a+1):
        if i < 10:
            i = str(i)
            x.append('0'+i)
        else:
            x.append(i)
    for k in range(1, n+1):
        for j in range(1, n+1):
            if  k == 1: # upper line
                if j == n:
                    print(x[j-1],  end = '')
                else:
                    print(x[j-1],  end = sep)
            elif k == n: # under line
                if j == n:
                    print(x[a-j-(n-2)],  end = '')
                else:
                    print(x[a-j-(n-2)],  end= sep)
            else: # midle line
                if j == 1:
                    print(x[-k+1], end= sep)
                elif j == n:
                    print(x[j+k-2],end='')
                else:
                    print(sep + sep, end = sep)
        print()


