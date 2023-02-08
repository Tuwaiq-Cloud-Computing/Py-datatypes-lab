# make a list of 3 dictionaries
people = [
    {"name": "Ahmed", "phone_number": "123456"},
    {"name": "Nasser", "phone_number": "654321"},
    {"name": "Mohammed", "phone_number": "111111"}
]

# add 1 more dictionary to the list
people.append({"name": "Omar", "phone_number": "222222"})

# delete the name from the first dictionary
del people[0]["name"]

# update the phone number of the last person
people[-1]["phone_number"] = "333333"

# check if the first dictionary has a key called "name"
print("name" in people[0])
