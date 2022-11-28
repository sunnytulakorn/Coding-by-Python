#630510582
#tulakorn sawangmuang
#Section-001
#Lab08_5
import string

def decode(code_table, text):
    line = len(code_table) # amount word
    x = code_table 
    y = text.replace('\n', ' \n ') # replace word
    z = y.split(' ') # skip
    for i in z:
        if i == '\n': #condition
            print()
        elif i.isdigit(): # condition if i is numbers
            for k in x:
                if x.find(k) == int(i): #condition
                    print(k, end ='')
                elif int(i) >= line: #condition
                    print('_',end='')
                    break # stop loop
        elif i =='': #condition
            continue # do loop
        else:
            print('_',end='') 
