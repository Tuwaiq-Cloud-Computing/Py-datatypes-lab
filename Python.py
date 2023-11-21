#Make a list with 3 elements
mylist = ["paris", "Seoul", "London"]
#add an element to the end of list
mylist.append("Dubai")
#remove an element from the list
mylist.remove("Seoul")
print(mylist)
#reverse the list
mylist.reverse()
print(mylist)
#sort the list
mylist.sort()
print(mylist)
#add an element at the start of the list
mylist.insert(0,"Riyadh ")
print(mylist)

#print the index of the last element
print(mylist[-1])
#______________________________________________
people = ["Ahmed", "Nasser", "Mohammed"]
print(people)
#print the list in the following format: Ahmed, Nasser, Mohammed
people_for = ','.join(people)
print(people_for)

#______________________________________________
contacts = [
    {"name": "Raghad", "phone_number": "0506238232"},
    {"name": "Sara", "phone_number": "0506238232"},
    {"name": "Ahmed", "phone_number": "0506238232"}
]
# Add a new dictionary to the list
contacts.append({"name": "amal", "phone_number": "0504398276"})
# Delete the name from the first dictionary
del contacts[0]["name"]
# Update the phone number of the last person
contacts[-1]["phone_number"] = "0506378467"
# Check if the first dictionary has a key called "name"
has_name_key = "name" in contacts[0]
print(contacts)
print("Does the first dictionary have a key called 'name'? ", has_name_key)
