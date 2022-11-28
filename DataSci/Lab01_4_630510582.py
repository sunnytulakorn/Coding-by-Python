#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab01_4

def to_seconds(d, h, m, s):
    day = int(d)*86400 #convert day to sec
    hour = int(h)*3600 #convert hour to sec
    minute = int(m)*60 #convert minute to sec
    sec = int(s) # second value
    sum_ = day + hour + minute + sec # sum second
    print(sum_)

def main():
    d, h, m, s = input().split(",")
    to_seconds(d, h, m, s)
    main() # recursive main

if __name__ == "__main__":
    main()