#630510582
#tulakorn sawangmuang
#Section-001
#Lab13_2

def power_set(set_a): # nonzero ได้ไงไม่รู้ครับหรือใช้recursionไม่ได้
    if not set_a: # not set_a
        return [set()] # {}
    
    ans = [] # kep value
    for i in set_a:
        ss = set((i,))
        for j in power_set(set_a - ss): # recursion 
            if j not in ans: 
                ans.extend([j, j|ss]) # | is or to combine the set
    return (ans)
    
def main():
    set_a = {'a', 'b', 'c'}  
    print(power_set(set_a))

if __name__ == "__main__":
    main()   