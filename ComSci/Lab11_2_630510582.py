#630510582
#tulakorn sawangmuang
#Section-001
#Lab11_2
import copy

def remove_row_col(list_a, row, col):
    a = copy.deepcopy(list_a) # copy list_a
    b = len(list_a) # row
    c = len(list_a[0]) # col
    if row < b and row >= -b: # condition
        del a[row] # delete row
    if col < c and col >= -c: # condition
        for i in range(len(a)): # loop run 
            del a[i][col] # delete col
    return a

def main():
    list_a = [[2, 3, 4, 5],
[8, 7, 6, 5],
[0, 1, 2, 3]]
    row = 1
    col = -3
    print(remove_row_col(list_a, row, col))

if __name__ == "__main__":
    main()
