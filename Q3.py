people = [
    {"name": "Ahmed", "phone_number": "1234567890"},
    {"name": "Nasser", "phone_number": "0987654321"},
    {"name": "Mohammed", "phone_number": "1122334455"},
]

people.append({"name": "Ali", "phone_number": "5566778899"})

del people[0]["name"]

people[-1]["phone_number"] = "2233445566"
has_name_key = "name" in people[0]

print(people)
print("Does the first dictionary have a key called 'name'? ", has_name_key)