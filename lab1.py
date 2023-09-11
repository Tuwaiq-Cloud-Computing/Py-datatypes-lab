# Q1
x = [1, 2, 3]
print(x)
x.append(4)
print(x)
x.remove(2)
print(x)
x.reverse()
print(x)
x.sort()
print(x)
x.insert(0, 0)
print(x)
l = len(x) - 1
print(l)

# Q2
print("-------------------------")

people = ["Ahmed", "Nasser", "Mohammed"]
format= ", ".join(people)
print(format)

#Q3
print("-------------------------")

info = [
    {"name": "Rahaf", "phonenum": "090754"},
    {"name": "Rawaa", "phonenum": "876564"},
    {"name": "Shouq", "phonenum": "098765"}
]

info.append({"name": "sara", "phonenum": "7999807"})
del info[0]["name"]
info[-1]["phonenum"] = "123456"
if "name" in info[0]:
    print("The first dictionary has 'name'")
else:
    print("The first dictionary does not have a'name'")

print("-------------------------")
