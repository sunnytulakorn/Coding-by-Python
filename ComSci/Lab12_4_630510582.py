#630510582
#tulakorn sawangmuang
#Section-001
#Lab12_4
import copy
def polynomial_addition(p1, p2):
    sp1 = copy.deepcopy(p1) # copy
    sp2 = copy.deepcopy(p2) # copy
    sp1.sort() # sort sp1
    sp1.reverse() # reverse sp1
    sp2.sort() # sort sp2
    sp2.reverse() # reverse sp2
    ans = []
    if len(sp1) == len(sp2) or len(sp1) > len(sp2): # condition sp1 
        for i in sp1:
            p = 0
            re = [] # keep value
            for j in sp2:
                if i[0] == j[0]: # if first value is same
                    if i[1] + j[1] != 0:
                        re.append(i[0])
                        p += i[1] + j[1]
                        re.append(p)
                        tu = tuple(re) # change to tuple
                        ans.append(tu) 
    elif len(sp2) > len(sp1): # condition sp2
        for i in sp2:
            p = 0
            re = [] # keep value
            for j in sp1:
                if i[0] == j[0]: # if first value is same
                    if j[1] + i[1] != 0:
                        re.append(i[0])
                        p += j[1] + i[1]
                        re.append(p)
                        tu = tuple(re) # change to tuple
                        ans.append(tu)
    for i in ans:
        for j in sp1:
            if i[0] == j[0]: # if first value is same 
                sp1.remove(j)
    for i in ans:
        for j in sp2:
            if i[0] == j[0]: # if first value is same 
                sp2.remove(j)
    if len(sp1) > len(sp2) or len(sp1) == len(sp2): # condition 
        for i in sp1:
            for j in sp2:
                if i[0] == j[0]: # if first value is same 
                    sp1.remove(i) # remove to update value
                    sp2.remove(j) # remove to update value
    elif len(sp2) > len(sp1): # condition
        for i in sp2:
            for j in sp1:
                if i[0] == j[0]: # if first value is same 
                    sp2.remove(i) # remove to update value 
                    sp1.remove(j) # remove to update value
    if sp1 > [] and sp2 == []: # condition
        ans.extend(sp1)
    elif sp1 == [] and sp2 > []: # condition
        ans.extend(sp2)
    elif sp1 > [] and sp2 > []: # condition 
        ans.extend(sp1)
        ans.extend(sp2)
    ans.sort(reverse=True) # sort and reverse answer
    return ans

def main():
    p1 =[(2, 6), (1, 34), (0, -8)]
    p2 = [(2, -6), (0, 2), (1, 1)]
    print(polynomial_addition(p1, p2))
if __name__ == '__main__':
    main()