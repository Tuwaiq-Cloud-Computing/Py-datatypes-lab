


#Q1
list = ['Apple','Orange','Cherry']
list.append('Straubery')
print(list)
list.remove('Apple')
print(list)
list.reverse()
print(sorted(list))
list.insert(0,'Rosebery')
print(list)
print(len(list) - 1)

#Q2
people = ["Ahmed", "Nasser", "Mohammed"]
M = ", ".join(people)
print(M)

#Q3
my_list = [
    {"name": "John", "phone_number": "123456789"},
    {"name": "Jane", "phone_number": "987654321"},
    {"name": "Alice", "phone_number": "555555555"}
]
print(my_list)

new_dict = {"name": "Bob", "phone_number": "999999999"}
my_list.append(new_dict)

del my_list[0]["name"]
print(my_list)

my_list[-1]["phone_number"] = "888888888"
print(my_list)


print("name" in my_list[0])