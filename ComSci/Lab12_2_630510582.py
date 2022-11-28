#630510582
#tulakorn sawangmuang
#Section-001
#Lab12_2

def search_event(list_x, key):
    for i in list_x:
        print(list_x[i])

def main():
    list_x = [("11/1/1900", "Event A"), ("5/12/2001", "Event B"),("5/12/2002", "Event C"), ("21/8/2008", "Event D"),("9/3/2013", "Event E"), ("11/3/2017", "Event F"),("7/5/2019", "Event G"), ("29/2/2032", "Event H"),("9/11/2042", "Event I")]
    event = search_event(list_x, "29/02/2032")
    print("---")
    print(event)

if __name__ == "__main__":
    main()