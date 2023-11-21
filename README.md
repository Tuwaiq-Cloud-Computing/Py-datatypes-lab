

items = ["Ahmad", "Nasser", "Mohammed"]
print(items)

items.append("Fay")
print(items)

items.remove("Nasser")
print(items)

items.reverse()
print(items)

items.sort()
print(items)

items.insert(0, "Shahad")
print(items)

last_index = len(items) - 1
print("Index of last element:", last_index)
print(items)

people = ["Ahmad", "Nasser", "Mohammed"]

formatted_list = ','.join(people)
print(formatted_list)

people_list = [
    {"name": "Amal", "phone_number": "0534567890"},
    {"name": "Huda", "phone_number": "0546543210"},
    {"name": "Yara", "phone_number": "0538901234"}
]
print(people_list)

people_list.append({"name": "Lolo", "phone_number": "0567890123"})
print(people_list)

del people_list[0]["name"]
print(people_list)

people_list[-1]["phone_number"] = "0535555555"
print(people_list)

has_name_key = "name" in people_list[0].keys()
print("Does the first dictionary have a key called 'name'?", has_name_key)

