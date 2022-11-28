#630510582
#tulakorn sawangmuang
#Section-001
#Lab08_EX1

def xmas_tree(n):
    if abs(n) != 0:
        s1 = 2+n # tree top space
        a = 1 # part of the tree
        w = a # Edge distance of the tree
        s = 1+n # space
        bus = s # Edge distance
        b = 3+n # base
        ans = '\n' # keep answer
        ans += s*' '+'   |' + '\n'
        ans += s*' '+' --*--'  + '\n'
        ans += s1*' '+' /|\\ ' + '\n'
        ans += s1*' '+'/* *\\ ' + '\n'
        for _ in range (1,n+1):
            for _ in range (1,4):
                ans += (s*' '+'/*'+' '+a*'* '+'*\\ ' ) + '\n' # body Apart from print
                a = a+1
                s = s-1
            w += 1
            a = w
            bus -= 1
            s = bus
        ans += b*' '+'|||'+b*' ' + '\n'
        ans += b*'_'+'|||'+b*'_' + '\n'
    return ans # display answer

def main():
    n = int(input())
    answer = xmas_tree(n)
    print(answer)

if __name__ == '__main__' :
    main()    