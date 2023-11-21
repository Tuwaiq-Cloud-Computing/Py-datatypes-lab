# Question 1:

# Make a list with 3 elements
list = ['first', 'second', 'third']

# add an element to the end of list
list.append('forth')
print(list)

# remove an element from the list
list.pop()
print(list)

# reverse the list
list.reverse()
print(list)

# sort the list
list.sort()
print(list)

# add an element at the start of the list
list.insert(0, "zero")
print(list)

# print the index of the last element
print(len(list)-1)


# Question 2:
people = ["Ahmed", "Nasser", "Mohammed"]

# print the list in the following format: Ahmed, Nasser, Mohammed
print(', '.join(people))


# Question 3:

dictionaryList = [{
    "name": "Ali",
    "phone_number": "055550"
}
,
{
    "name": "Maha",
    "phone_number": "055551"
}
,
{
    "name": "Nourah",
    "phone_number": "055552"
}]

# add 1 more dictionary to the list

dictionaryList.append({"name": "Khalid", "phone_number": "055553"})
print(dictionaryList)

# delete the name from the first dictionary

del dictionaryList[0]["name"]
print(dictionaryList)

# update the phone number of the last person

dictionaryList[(len(dictionaryList)-1)]["phone_number"]= "050000"
print(dictionaryList)

# check if a first dictionary has a key called "name"

if "name" in dictionaryList[0]:
    print("yes, first dictionary has a key called name")
else:
    print("no, first dictionary has no key called name")