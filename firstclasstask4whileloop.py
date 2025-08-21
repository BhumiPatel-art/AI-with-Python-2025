total_balance = 15000;
print("welcome to your bank")
print("1. Deposite your amount.")
print("2. withdrow your amount.")
print("3. check your balance.")
print("4. Exit")
num=int(input("enter your choice:"))
if num==3:
    print(f"your balance is:{total_balance}")
if num==2:
    amount=int(input("enter your amount:"))
    while amount >= 1000:
        print(f"Here you collect your money:")
if num==1:
    amount=int(input("enter your amount:"))
    while amount >= 1000:
        print(f"add your money:")
    else:
        print(f"you only able to add more then 1000rs:")