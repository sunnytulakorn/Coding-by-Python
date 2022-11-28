#630510582
#tulakorn sawangmuang
#Section-001
#Lab13_3
import string 
def word_count(text):
    x = text.split()
    ans = {}
    for i in x :
        if i[0] not in string.punctuation:
            ans += [i]
        else:
            if i[0] in string.punctuation:
                x = i[0].replace('')
            if i[(len(i)-1)] in string.punctuation:
                i[(len(i)-1)].replace('')
            ans += [i]
    return ans
            

def main():
    text = "He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."
    print(word_count(text))

if __name__ == "__main__":
    main()