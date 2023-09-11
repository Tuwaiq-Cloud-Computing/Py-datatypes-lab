

#Quwstion 1:

#1- Make a list with 3 elements
list = ['A', 'B', 'C' , 'D']
print(list)

#2- Add an element to the end of the list
list.append('E')
print(list)
#3-Remove an element from the list
list.remove('C')
print(list)
#4-Reverse the list
list.reverse()
print(list)
#5-Sort the list
list.sort()
print(list)
#6-Add an element at the start of the list
list.insert(0, 'H')
print(list)
#7-Print the index of the last element
last_index = len(list) - 1
print(last_index)


#Question 2
people = ["Ahmed", "Nasser", "Mohammed"]
newlist = ", ".join(people)
print(newlist)

#Question 3

# Make a list of 3 dictionaries, each containing name and phone_number
listp = [
    {"name": "Alaa", "phone_num": "666 666 6666"},
    {"name": "Sama", "phone_num": "777 777 7777"},
    {"name": "Lujain", "phone_num": "888 888 8888"}
]

# Add one more dictionary to the list
listp.append({"name": "Rawan", "phone_num": "111 111 1111"})
print(listp)

# Delete the name from the first dictionary
del listp[0]["name"]
print(listp)

# Update the phone number of the last person
listp[-1]["phone_num"] = "999 999 9999"
print(listp)

# Check if the first dictionary has a key called "name"
if "name" in listp[0]:
    print("The first dictionary has a key called 'name'")
else:
    print("The first dictionary does not have a key called 'name'")
