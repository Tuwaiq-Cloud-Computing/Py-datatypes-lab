
#Question1
list = ['Raneem','Amjad','Sara']
list.append('Emtenan')
print(list)
list.remove('Raneem')
print(list)
list.reverse()
print(sorted(list))
list.insert(0,'Noura')
print(list)
print(len(list) - 1)

#Question2
people = ["Ahmed", "Nasser", "Mohammed"]
M = ", ".join(people)
print(M)

#Question3
my_list = [
    {"name": "raneem", "phone_number": "0544558828"},
    {"name": "amjad", "phone_number": "0544559999"},
    {"name": "noura", "phone_number": "0544558888"}
]
print(my_list)

new_dict = {"name": "juju", "phone_number": "0544557777"}
my_list.append(new_dict)

del my_list[0]["name"]
print(my_list)

my_list[-1]["phone_number"] = "0544556666"
print(my_list)


print("name" in my_list[0])
