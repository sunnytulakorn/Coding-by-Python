#630510582
#tulakorn sawangmuang
#Section-001
#Lab13_4
import copy
def square_matrix(list_x):
    x = 0 # keep len col
    zero = 0 # Determinant to plus 0
    for i in range(len(list_x)): 
        col = len(list_x[i])
        if col > x:
            x = col
    if len(list_x) > x: # compare col and row
        zero += len(list_x)
    else:
        zero += x
    matrix = []
    for i in range(zero - len(list_x)): # col loop
        for j in range(zero):
            matrix.append(0) # plus 0
        select = copy.deepcopy(matrix) # copy
        list_x.append(select) # add 0 to matrix
        matrix = [] # reset list to do next col loop    
    for i in list_x: # row loop
        for j in range(zero - len(i)):
            i.append(0)
    
    
def main():
    list_x = [[2, 3, 4],[1, 2, 3]]
    print(square_matrix(list_x))

if __name__ == "__main__":
    main()
