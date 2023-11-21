
my_list = [1, 2, 3]
my_list.append(4)
my_list.remove(2)
my_list.reverse()
my_list.sort()

my_list.insert(0, 0)


print(my_list.index(my_list[-1]))
people = ["Ahmed", "Nasser", "Mohammed"]
formatted_list = ", ".join(people)
print(formatted_list)

my_list = [
    {"name": "John", "phone_number": "123456789"},
    {"name": "Jane", "phone_number": "987654321"},
    {"name": "Bob", "phone_number": "567890123"}
]

my_list.append({"name": "Alice", "phone_number": "456789012"})


del my_list[0]["name"]


my_list[-1]["phone_number"] = "111111111"

has_name_key = "name" in my_list[0]

print(my_list)
print(has_name_key)