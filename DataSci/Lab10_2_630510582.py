#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab10_2
import string

def make_list_clean(list_x): #delete the first&last of each word if it not alphabet
    ans = []
    for i in list_x:
        j = i.strip(',')
        ans.append(j.strip('.').strip('$').lower())
        for i in range(len(ans)):
            ans[i] = ans[i].strip(string.punctuation)
    return ans

def word_count(text):
    ans = dict()
    list_ = text.split(' ')
    list_word = make_list_clean(list_)
    for i in list_word:
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1
    return ans

def main():
    text = "He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."
    print(word_count(text))

if __name__ == "__main__":
 main()
