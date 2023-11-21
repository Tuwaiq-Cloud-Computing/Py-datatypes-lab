
people = ["John", "Bob", "Alic"]

people.append("lyla")
print(people)

removed_person = people.pop(1)
print(people)

people.reverse()
print(people)

people.sort()
print(people)

people.insert(0, "Jaim")
print(people)

last_element_index = len(people) - 1
print("Index of the last element:", last_element_index)



people = ["John", "Bob", "Alic"]
print(people)

formatted_list = ','.join(people)
print("Formatted List:", formatted_list)


people_info = [
    {"name": "John", "phone_number": "051234565"},
    {"name": "Bob", "phone_number": "057890127"},
    {"name": "Alic", "phone_number": "053456789"}
]

people_info.append({"name": "Alice", "phone_number": "05555555"})
print(people_info)



del people_info[0]["name"]
print(people_info)


has_name_key = "name" in people_info[0]
print(people_info)


people_info[-1]["phone_number"] = "05999999"
print(people_info)

has_name_key = people_info[0].get("name") is not None
print("First dictionary has 'name' key:", has_name_key)



