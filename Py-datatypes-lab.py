print("Py-datatypes-lab")

print("Question 1")

myList = people = ["Basil", "Hani", "Mohammed"]

print("my list : ",myList)

#add an element to the end of list
myList.append("Ali")
print(myList)


# remove an element from the list
myList.remove("Hani")
# reverse the list
myList.reverse()
print(myList)
# sort the list
myList.sort()
print("myList.sort()",myList)
# add an element at the start of the list
myList.insert(0,"ALBASIL")
print(myList)
# print the index of the last element
print(myList[-1])


print('\n------------------------------------------------------------------\n')

print("Question 2")

people = ["Ahmed", "Nasser", "Mohammed"]
#1-print the list in the following format: Ahmed, Nasser, Mohammed 2
[print(x) for x in people]

print("***************************")
#2-print the list in the following format: Ahmed, Nasser, Mohammed
for name in people:
    print(name)

print('\n------------------------------------------------------------------\n')


print("Question 3")


#
# Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number


my_dictionary =[{
  "name": "ALBASIL",
  "phone_number": "0569861476",
},{
  "name": "Basil",
  "phone_number": "0569861476",
},{
  "name": "Hain",
  "phone_number": "0569861476",
}]

print(my_dictionary)


# now add 1 more dictionary to the list

my_dictionary.append({
  "name": "Ahmed",
  "phone_number": "0569861476",
})
print(my_dictionary)


# now delete the name from the first dictionary

my_dictionary[0].pop('name')
print(my_dictionary)


# update the phone number of the last person
my_dictionary[-1]['phone_number']='055551419'
print(my_dictionary)


# check if a first dictionary has a key called "name"

my_dictionary[0]


if 'name' in my_dictionary[0]:
    # first dictionary has a key called "name"
    print('The first dictionary has a key called "name"')
else:
    print('The first dictionary does not have a key called "name"')