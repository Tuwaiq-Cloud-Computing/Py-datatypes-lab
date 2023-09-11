
#Question 1:

my_list=[10, 20, 30]
print(my_list)
my_list.append(40)
print(my_list)
my_list.remove(30)
print(my_list)
output=my_list[::-1]
print(output)
my_list.sort()
print(my_list)
my_list.insert(0, 5)
print(my_list)
last_element_index=len(my_list)-1
print(last_element_index)

#Question 2:

people = ["Ahmed", "Nasser", "Mohammed"]
print(people)
formatted_list=", ".join(people)
print(formatted_list)

#Question 3:

people_list = [
{"name": "Wjoud", "phone_number": "0505050505"},
{"name": "Noor", "phone_number": "0555505555"},
{"name": "Hindi", "phone_number": "0550550550"}
]
print(people_list)
people_list.append({"name": "Waled", "phone_number": "0555555555"})
print(people_list)
del people_list[0]["name"]
print(people_list)
people_list[-1]["phone_number"] = "0567805678"
print(people_list)

if "name" in people_list[0]:
 print("The first dictionary has a key called 'name'")
else:
 print("The first dictionary does not have a key called 'name'")
 