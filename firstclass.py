print(f"Welcome to voting things:")
age = int(input("enter your age "))
cs = str(input("enter your Citizenship:"))
if age >= 18 and cs == "true":
    print(f"Congratulations you are eligable for votting")
if age < 18 and cs == "true":
    print(f"Sorry You are not eligable for voting")
if age >= 18 and cs == "false":
    print(f"Sorry You have no rights for votting")


