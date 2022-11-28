#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab06_5
import string

def check_palindrome(text):
    new_text = ''
    for i in text:
        if i in string.ascii_letters:
            new_text += i
    new_text = new_text.lower()
    if(new_text == new_text[::-1]):
        return True
    else:
        return False

def main():
    text = input("Enter str: ")
    print(check_palindrome(text))
    main()

if __name__=="__main__":
    main()