#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab10_1

import string

def count_letter(text):
    count = 0 
    str_ = "AEIOU"
    for i in str_:
        text = text.upper()
        count += text.count(i)

    percentage = (count/len(text))*100

    print("Counting = {0:d} ({1:.2f}%)".format(count, percentage))

def read_file(filename,mode="rt"):  
    with open(filename) as fin:
        fin = open(filename, mode, encoding='utf-8')
        contents = fin.read()
 
    return contents

def main():
    text_input = read_file("in_01.txt")
    text_input = text_input.strip()
    count_letter(text_input)

if __name__=="__main__":
    main()