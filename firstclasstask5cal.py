n1 = int(input("enter your first number:"))
n2 = int(input("enter your second number:"))

print("enter your choice")

o1= print("1.you want to do addition:")
o2=print("2. you want to do subtraction:")
o3=print("3. you want to do multiplication:")
o4=print("4. you want to do division:")
choice=int(input("enter your choice:"))
def addition():
    t1= n1 + n2
    return t1
def subtraction():
    t1= n1 - n2
    return t1
def multiplication():
    t1= n1 * n2
    return t1
def division():
    t1= n1 / n2
    return t1

if choice==1:
    print(addition())
elif choice==2:
    print(subtraction())
elif choice==3:
    print(multiplication())
elif choice==4:
    print(division())
else:
    print("enter valid choice")


