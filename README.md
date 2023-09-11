# Py-datatypes-lab

## Tasks:

Question 1:
- Make a list with 3 elements
  fruits = ['banana', 'apple', 'orange']
print(fruits)

- add an element to the list
fruits.append('berry')
print(fruits)

- remove an element from the list
  fruits.remove('banana')
print(fruits)

- reverse the list
fruits.reverse()
print(fruits)

- sort the list
  fruits.sort()
print(fruits)

- add an element at the start of the list
  fruits.insert(0, 'mango')
print(fruits)

- print the index of the last element
last_index = len(fruits) - 1
print(last_index)

Question 2:
Consider the following list: ``` people = ["Ahmed", "Nasser", "Mohammed"] ```
- print the list in the following format: Ahmed, Nasser, Mohammed
- hint: read about join()

people = ["Ahmed", "Nasser", "Mohammed"]

formatted_list = ", ".join(people)
print(formatted_list)

Question 3:
- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
  list = [
    {"Name": "Amal", "Phone_number": "055644321"},
    {"Name": "Noura", "Phone_number": "056888743"},
    {"Name": "Ali", "Phone_number": "055789763"}
]
print(list)

- now add 1 more dictionary to the list
  list.append({"Name": "Khalid", "Phone_number": "055676521"})
print(list)

- now delete the name from the first dictionary
  del list[0]["Name"]
print(list)

- update the phone number of the last person
  list[-1]["Phone_number"] = "055558876"
print(list)

- check if a first dictionary has a key called "name" 
if "Name" in list[0]:
    print("The first dictionary has a key called 'Name'")
else:
    print("The first dictionary does not have a key called 'Name'")

## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.
