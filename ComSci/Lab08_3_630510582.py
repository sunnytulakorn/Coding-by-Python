#630510582
#tulakorn sawangmuang
#Section-001
#Lab08_3

import string

def patterned_message(message, pattern):
    x = message.replace(' ', '') # word to replace
    while len(pattern) > 0: # loop
        for i in x:
            for j in pattern:
                if j == '*': # when is * 
                    print(j.replace('*',i),end='') # replace Until the end
                    pattern = pattern[1:] # relace word
                    break # stop loop
                if j == '\n': # when is new line
                    print()
                    pattern = pattern[1:] # relace word
                if j ==' ': # when is nothing(space)
                    print(' ',end='')
                    pattern = pattern[1:] # relace word

def main():
    message = input()
    pattern = input()
    patterned_message(message, pattern)

if __name__ == "__main__":
    main()
