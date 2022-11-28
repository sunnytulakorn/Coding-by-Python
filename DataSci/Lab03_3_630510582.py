#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab03_3

def credit_balance(price, n, money):
    paid = price*n
    print("%.1f*%d=%.1f"%(price,n,paid))
    money_paid = money - paid
    if money_paid >= 0:
        print(money_paid)
    else:
        print("Not enough money")

def main():
    price = float(input("Enter price: "))
    n = int(input("Enter n: "))
    money = float(input("Enter money: "))
    credit_balance(price, n, money)

if __name__=="__main__":
    main()