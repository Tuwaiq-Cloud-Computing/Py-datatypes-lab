list=[1,2,3]
list.append("a")
print(list)
del list[3]
print(list)
list.reverse()
print(list)
list.sort()
print(list)
list.insert(0,"m")
print(list)

print(list.index(3))
people=["Ahmed","Nasser","Mohammed"]
var=","
print(var.join(people))
dict=[
    {"name":"maram","phone":"2345667"},
    {"name":"noha","phone":"678899"},
    {"name":"maha","phone":"11111117"}
]
print(dict)
dict.append({"name":"lila","phone":"45674"})
print(dict)
del dict[0]["name"]
print(dict)
dict[-1]["phone"]="00000"
print(dict)
if "name" in dict[2]:
    print("exist")
else:
    print("the name dosen't exist")