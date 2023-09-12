
# Q1----------------------------------------

list = [1, 2, 3]
list.append(4)
list.remove(2)
list.sort()
list.insert(0, 6)
last_element_index = len(list) - 1
print(last_element_index)
print(list)

# Q2-----------------------------------------
people = ["ahmed", "nasser", "mohammed"]
formatted_list = ", ".join(people)
print(formatted_list)

# Q3----------------------------------------
list3 = [
    {"name": "Lolo", "Number": "055679"},
    {"name": "Sara", "Number": "056798"},
    {"name": "Nora", "Number": "555555"}
]
list3.append({"name": "Sultan", "Number": "0588888"})
del list3[0]["name"]

list3[-1]["number"] = "88888"
if "name" in list3[0]:
    print("the first dic has key 'NAME'")
else:
    print("the first dic dose not have a key 'NAME'")
