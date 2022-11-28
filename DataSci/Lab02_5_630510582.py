#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab02_5

def net_price(price1, price2, price3):
    d1 = 5/100
    d2 = 10/100
    d3 = 20/100
    item1 = cal_price(price1, d1)
    item2 = cal_price(price2, d2)
    item3 = cal_price(price3, d3)
    total_ = item1 + item2 + item3
    print("%.2f %.2f %.2f %.2f"%(item1,item2,item3,total_))

def cal_price(price, discount):
    return(price - price*discount + (((price - price*discount)/100)*7))

def main():
    price1 = int(input())
    price2 = int(input())
    price3 = int(input())
    net_price(price1, price2, price3)
    main()

if __name__=="__main__":
    main()