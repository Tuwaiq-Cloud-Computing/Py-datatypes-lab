# Question 1:
#     Make a list with 3 elements
list = [4, 6, 3]
#     add an element to the end of list
list.append(9)
#     remove an element from the list
list.pop()
#     reverse the list
list.reverse()
#     sort the list
list.sort()
#     add an element at the start of the list
list.insert(0, 5)
#     print the index of the last element
print(list[-1])


# Question 2: Consider the following list: people = ["Ahmed", "Nasser", "Mohammed"]
#     print the list in the following format: Ahmed, Nasser, Mohammed
#     hint: read about join()
people = ["Ahmed", "Nasser", "Mohammed"]
print(', '.join(people))


# Question 3:
#     Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
myInfo = {
    0: {"name": "abdulmajeed", "phone_number": "0500000000"},
    1: {"name": "ahmed", "phone_number": "0500000100"},
    2: {"name": "khaled", "phone_number": "0500000600"},
}

#     now add 1 more dictionary to the list
myInfo[3] = {"name": "majid", "phone_number": "0583848549"}

#     now delete the name from the first dictionary
del myInfo[0]["name"]

#     update the phone number of the last person
myInfo[3]["phone_number"] = "0566666666"

#     check if a first dictionary has a key called "name"
print("name" in myInfo)
