# Py-datatypes-lab

## Tasks:

Question 1:
- Make a list with 3 elements
- - list = [1, 2, 5]
- add an element to the end of list
- - list.append("7")
- remove an element from the list
- - del list[0]
- reverse the list
- -  list.reverse()
- sort the list 
- - list.sort()
- add an element at the start of the list
- -  list.insert(0, 0)
- print the index of the last element
- - index = len(list) - 1

Question 2:
Consider the following list: ``` people = ["Ahmed", "Nasser", "Mohammed"] ```
- print the list in the following format: Ahmed, Nasser, Mohammed
- hint: read about join()
- - people = ["Ahmed", "Nasser", "Mohammed"]

x = ", ".join(people)

print(x)


Question 3:
- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
list_of_dictionaries = [
  {
    "name": "m",
    "phone_number": "9440"
  },
  {
    "name": "m",
    "phone_number": "050510"
  },
  {
    "name": "mm",
    "phone_number": "044485"
  }
]- now add 1 more dictionary to the list 
list_of_dictionaries.append({
  "name": "nnn",
  "phone_number": "5555"
})- now delete the name from the first dictionary
for dictionary in list_of_dictionaries:
  print(dictionary["name"], dictionary["phone_number"])
  
  - update the phone number of the last person
list_of_dictionaries[-1]["phone_number"] = "050000000"

- check if a first dictionary has a key called "name" 
if "name" in list_of_dictionaries[0]:
  print("The first dictionary has a key called 'name'.")
else:
  print("The first dictionary does not have a key called 'name'.")
## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.
