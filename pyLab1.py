
list = ["A", "B", "C"]

list.append("D")
print(list)

del list[0] 
print(list)

list.reverse()
print(list)

list.sort()
print(list)

list.insert(0, 1)
print(list)



print(list.index(list[-1]))

print("--------------------------------------------")
people = ["Ahmed", "Nasser", "Mohammed"]
formatted_list = ", ".join(people)
print(formatted_list)
print("--------------------------------------------")

Plist = [
    {"name": "John", "phone_number": "0547895474"},
    {"name": "Jane", "phone_number": "0541237895"},
    {"name": "Bob", "phone_number": "0541789541"}
]

Plist.append({"name": "Alice", "phone_number": "0569842357"})


del Plist[0]["name"]


Plist[-1]["phone_number"] = "0547171789"

has_name_key = "name" in Plist[0]

print(Plist)
print("--------------------------------------------")

print(has_name_key)
