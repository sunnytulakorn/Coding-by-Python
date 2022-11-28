#630510582
#tulakorn sawangmuang
#Section-001
#Lab08_4

import string

def uniform_small(line):
    return sum(1 for s in line if s.islower()) # plus 1 in sum when the word is lower

def uniform_large(line):
    return sum(1 for l in line if l.isupper()) # plus 1 in sum when the word is upper
    
def uniform(line):
    small = uniform_small(line) # small value
    large = uniform_large(line) # large value
    if small > large: # condition to display answer
        answer = (line.lower())
    elif small == large: # condition to display answer
        b = line[0]
        if b == b.upper(): # condition to display answer
            answer = (line.upper())
        else: # condition to display answer 
            answer = (line.lower())
    else: # condition to display answer
        answer = (line.upper())
    return answer
    

def main():
    line= input() # input word
    ans = uniform(line) # display answer equation
    print(ans) # display answer

if __name__ == "__main__":
    main()

