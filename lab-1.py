#Q1
# Make a list with 3 elements
q1= [1, 9,3 ]

# Add an element to the end of the list
q1.append(4)


q1.remove(9)


q1.reverse()


q1.sort()


q1.insert(0, 0)

last_index = len(q1) - 1
print(last_index)

# Q2

people = ["Ahmed", "Nasser", "Mohammed"]
formatted_list = ", ".join(people)
print(formatted_list)



#Q3
people_list = [
    {"name": "Futun", "phone_number": "0580303038"},
    {"name": "rahaf", "phone_number": "0567686492"},
    {"name": "ghada", "phone_number": "0578382288"}
]

people_list.append({"name": "mohammed", "phone_number": "0589392928"})


del people_list[0]["name"]


people_list[-1]["phone_number"] = "111-222-3333"


if "name" in people_list[0]:
    print("The first dictionary has a key called 'name'")
else:
    print("The first dictionary does not have a key called 'name'")
