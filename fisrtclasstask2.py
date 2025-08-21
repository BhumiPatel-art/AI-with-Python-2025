print(f"Get Knowledge about your medical report:")
age = int(input("Age: "))
if age <= 18 and age > 15:
    weight = int(input("Weight: "))
    if weight >= 55:
        print(f"patient is aligible to getting a mediciens")
    else:
        print(f"patient is not aligible to getting a mediciens")
else:
    print(f"patient is not aligible to getting a mediciens")