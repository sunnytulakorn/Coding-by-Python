#630510582
#tulakorn sawangmuang
#Section-001
#Lab07_EX2

def pyramid_stairs(n):
    n > 0
    n = abs(n)
    round = 22
    x = 2
    x1 = 1
    y = 0
    y1 = 10
    if n == 1:
        print('  ' + 'o' + '  ' + 12*'*' + '  ' + 'o') # head part
        print(' ' + '/' + '|' + '\\' + ' ' + '*' + 10*' '+ '*' + ' ' + '/' + '|' + '\\') # body part
        print(' ' + '/' + ' ' + '\\' + ' ' + '*' + 10*' '+ '*' + ' ' + '/' + ' ' + '\\') # bottom part
    if n != 1: # morn than 1 floor
        for i in range(1, n):
            round += 10 # plsu to increase base
            x += 5 # plus for Edge distance top floor
            x1 += 5 # plus for Edge distance top floor
        for k in range(1, n+1):
            if k == 1: # top floor
                print(x*' ' + 'o'+'  '+ 12*'*' + '  '+ 'o') # head part top floor
                print(x1*' '+'/' + '|' + '\\' + ' ' + '*' + 10*' ' +'*' +' '+ '/' + '|' + '\\') # body part top floor
                print(x1*' '+'/' + ' ' + '\\' + ' ' + '*' + 10*' ' +'*' +' '+ '/' + ' ' + '\\') # bottom part top floor
            elif k > 1: # under top floor
                print(x*' '+'o'+'  '+6*'*' + y*' '+ 6*'*' + '  '+'o') # head part under Upstairs
                print(x1*' '+'/' + '|' + '\\' + ' ' + '*' + y1*' ' +'*' +' '+ '/' + '|' + '\\') # body part under Upstairs
                print(x1*' '+'/' + ' ' + '\\' + ' ' + '*' + y1*' ' +'*' +' '+ '/' + ' ' + '\\') # bottom part under Upstairs
            y += 10 # plus to do next floor
            y1 += 10 # plus to do next floor
            x -= 5 # minus for Edge distance
            x1 -= 5 # minus for Edge distance
    if n != 0 :
        print(round * '*') # base

def main():
    n = int(input())
    pyramid_stairs(n)

if __name__ == "__main__":
    main()
