#630510582
#tulakorn sawangmuang
#Section-001
#Lab11_3
import copy
def is_magic_square(board):
    x = len(board) #row
    y = len(board[0]) #colux
    w = 0 #seclect value
    k = [] #value row
    e = [] #value col 1
    a = [] #value col 2
    q = [] #value 1 col
    l = [] #value board
    v = [] #value 1 to n**2
    for i in range(x): # loop 
        for j in range(y):
            w += board[i][j]
            l.append(w)
            w = 0
    for i in range(1,(y**2)+1):
        v.append(i)
        
    if y * x == y**2 and sorted(l) == v:
        for i in board:
            w += sum(i)
            k.append(w)
            w = 0
        for i in range(x):
            for j in range(y):
                t = board[j][i]
                e.append(t)
            r = copy.deepcopy(e)
            a.append(r)
            e = []
        for i in a:
            w += sum(i)
            q.append(w)
            w = 0
        p = 0#collec value
        h = []#list collec value Diagonal
        for i in range(y):
            w += board[i][p]
            p += 1
            h.append(w)
            w = 0
        h = sum(h) #tatal Diagonal
        p = y-1
        t = [] #list collec value Diagonal
        for i in range(y):
            w += board[i][p]
            p -= 1
            t.append(w)
            w = 0
        t = sum(t) #tatal Diagonal
        c = 0 #collec value
        d = 0 #collec value
        for i in k:#check value k
            if i == h and i == t:
                c += 1
        for i in q:#check value q
            if i == h and i == t:
                d += 1
        if h == t and k == q and c == y and d == y and c == d:
            return True
        else:
            return False
    else:
        return False

def main():
    board = [[7, 12, 14, 1],
 [2, 13, 11, 8],
 [9, 6, 4, 15],
 [16, 3, 5, 10]]
    print(is_magic_square(board))

if __name__=='__main__':
    main()

