# Py-datatypes-lab

## Tasks:

'''Question 1:

Make a list with 3 elements
add an element to the end of list
remove an element from the list
reverse the list
sort the list
add an element at the start of the list
print the index of the last element'''

list1 = [2, 0, 1]
print(list1)
list1.append(5)
print(list1)
del list1[3]
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.insert(0, 9)
print(list1)
print(list1[3])


'''Question 2: 

Consider the following list: people = ["Ahmed", "Nasser", "Mohammed"]

print the list in the following format: Ahmed, Nasser, Mohammed
hint: read about join()'''

people = ["Ahmed", "Nasser", "Mohammed"]
print(people)
print (*people, sep=", ")


'''Question 3:

Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
now add 1 more dictionary to the list
now delete the name from the first dictionary
update the phone number of the last person
check if a first dictionary has a key called "name"'''

Ldict = [
{"name": "Mohammed", "age": 30, "phone": 966501111234},
{"name": "Abdullah", "age": 42, "phone": 966501123546},
{"name": "Bader", "age": 30, "phone": 966504423546}
]

Ldict.append({"name": "Khaled", "age": 33, "phone": 966504334111})

del Ldict[0]["name"]

Ldict[3]["phone"]=966505511434

print("name" in Ldict[0])



































Question 1:
- Make a list with 3 elements
- add an element to the end of list
- remove an element from the list
- reverse the list
- sort the list 
- add an element at the start of the list
- print the index of the last element


Question 2:
Consider the following list: ``` people = ["Ahmed", "Nasser", "Mohammed"] ```
- print the list in the following format: Ahmed, Nasser, Mohammed
- hint: read about join()

Question 3:
- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
- now add 1 more dictionary to the list 
- now delete the name from the first dictionary
- update the phone number of the last person
- check if a first dictionary has a key called "name" 


## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.
