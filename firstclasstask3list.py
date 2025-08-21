name = ["Bhumi","saba","irum","aman","sneha"]
print(name)
name.append("Matti")
print(name)
name.remove("aman")
print(name)
name.insert(4,"dhanlaxmi")
print(name)

people = ["honey","prijisa"]
name.extend(people)
print(name)

f_index = name.index("honey")
print(f_index)
if "honey" in name:
    print(f"honey is availble in list and her index is {(name.index("honey"))}")
name.sort()
print(name)