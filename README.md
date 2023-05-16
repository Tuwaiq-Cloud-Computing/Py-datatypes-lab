# Py-datatypes-lab

## Tasks:

Question 1:
- Make a list with 3 elements
- add an element to the end of list
- remove an element from the list
- reverse the list
- sort the list 
- add an element at the start of the list
- print the index of the last element

#1 make a list of 3 elements
Q1List = [3, 0, 2]
#2 add an element to the end of the list: 
Q1List.append(1)
#3 remove an element from the list: 
Q1List.pop(1)
#4 reverse the list
Q1List.reverse()
#5 sort the list
Q1List.sort()
#6 add an element to the start of the list: 
Q1List.insert(0, 5)
#7 print the last index: 
print (len(Q1List)-1)

Question 2:
Consider the following list: ``` people = ["Ahmed", "Nasser", "Mohammed"] ```
- print the list in the following format: Ahmed, Nasser, Mohammed
- hint: read about join()

people = ["Ahmed", "Nasser", "Mohsmmed"]
print (*people, sep=", ")

Question 3:
- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
- now add 1 more dictionary to the list 
- now delete the name from the first dictionary
- update the phone number of the last person
- check if a first dictionary has a key called "name" 

#1 make a list of 3 dictionaries
Ldict = [
{"name": "Waleed", "age": 23, "phone": 966509897890},
{"name": "Ahmed", "age": 26, "phone": 966505234978},
{"name": "Khaled", "age": 30, "phone": 966553197564}
]

#2 add 1 dictionary to the list
Ldict.append({"name": "Saad", "age": 20, "phone": 966534972604})

#3 delete the name from first dictionary
del Ldict[0]["name"]

#4 update the phone of the last person
Ldict[3]["phone"]=966505552146

#5 check if the first dictionary has a key called "name"
print("name" in Ldict[0])


## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.
