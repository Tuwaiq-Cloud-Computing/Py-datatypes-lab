#Question 1:
list1 = ["nasser", "ibrahim", "abuhaimed"]
list1.append("0")
print(list1)
list1.remove("ibrahim")
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.insert(0, "Mr")
print(list1)
print(str(list1[2]))


#Question 2:
people = ["Ahmed", "Nasser", "Mohammed"]
comma = ", ".join(people)
print(comma)

#Question 3:
list = [
    {"name": "nasser", "phone_number": "0560030321"}, {"name": "ibrahim", "phone_number": "0555555555"}, {"name": "ahmed", "phone_number": "0500000000"}
    ]
list.append({"name": "basil", "phone_number": "0569861476"})
print(list)

list[0].pop('name')
print(list)

list[-1]['phone_number'] = "05999999"
print(list)

print("\n\n\n")
if "name" in list[0]:
    print('Exist')
else:
    print('Not Exit')
