"""  Question 1:  """
# Make a list with 3 elements
mylist = ['Riyad', 'Yousef', 'Almalki']

# add an element to the end of list
mylist.append('Saudi')
print(mylist)

# remove an element from the list
mylist.remove('Saudi')
print(mylist)

# reverse the list
mylist.reverse()
print(mylist)

# sort the list
mylist.sort(reverse=False)
print(mylist)

# add an element at the start of the list
mylist.insert(0, 'Eng')
print(mylist)

# print the index of the last element
lastIndex = mylist.index(mylist[-1])
print(lastIndex)
# or
print(len(mylist) - 1)

"""  Question 2:  """
people = ["Ahmed", "Nasser", "Mohammed"]
# print the list in the following format: Ahmed, Nasser, Mohammed
print(','.join(people))

"""  Question 3:  """
# Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
mydictionary= [
    {
        'name': 'Riyad',
        'phone_number': '05555555555555'
    },
    {
        'name': 'Ali',
        'phone_number': '054444444444'
    },
    {
        'name': 'Abdullah',
        'phone_number': '0533333333333'
    }
]

# now add 1 more dictionary to the list
mydictionary.append({'name': 'Khalid', 'phone_number': '052222222222'})
print(mydictionary)

# now delete the name from the first dictionary
del mydictionary[0]['name']
print(mydictionary)

# update the phone number of the last person
mydictionary[-1]['phone_number'] = '0566666666666'
print(mydictionary)

# check if a first dictionary has a key called "name"
if "name" in mydictionary[0]:
    print("Yep there is a key called name")
else:
    print("Nah no such thing as name")
