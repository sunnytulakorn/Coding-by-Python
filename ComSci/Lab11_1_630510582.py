#630510582
#tulakorn sawangmuang
#Section-001
#Lab11_1
import copy
def matrix_mult(m1, m2):
    multiply = 0 # value
    cross = [] # cross mulyiply
    coc = [] # another cross
    answer = [] # answer
    if len(m1[0]) == len(m2): # equation of matrix
        for i in range(len(m1)): # loop 1st
            for j in range(len(m2[0])): # loop 2nd
                multiply = 0 # keep value
                for k in range(len(m1[0])): # loop for multiply
                    multiply += m1[i][k] * m2[k][j] # Match to multiply
                cross.append(multiply) # plus value
            coc = copy.deepcopy(cross) #copy list
            answer.append(coc) # plus value
            cross = [] # reset list value
        return answer # display value
    else:
        return None # display value

def main():
    m1 = [[1, 2, 3],
[4, 5, 6]]
    m2 =[[7, 8],
[9, 10],
[11,12]]
    print(matrix_mult(m1, m2))

if __name__ == "__main__":
    main()
