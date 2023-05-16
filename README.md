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

#Question 1
my_list = [1, 2, 3]
print(my_list)
my_list.append(4)
print(my_list)
my_list.remove(2)
print(my_list)
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)
my_list.insert(0, 0)
print(my_list)
print(my_list.index(my_list[-1]))
ر


Question 2:
Consider the following list: ``` people = ["Ahmed", "Nasser", "Mohammed"] ```
- print the list in the following format: Ahmed, Nasser, Mohammed
- hint: read about join()

#Qeustion 2

people = ["Ahmed", "Nasser", "Mohammed"]
format_list = ", ".join(people)
print(format_list)

Question 3:
- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
- now add 1 more dictionary to the list 
- now delete the name from the first dictionary
- update the phone number of the last person
- check if a first dictionary has a key called "name" 

#Qeustion 3 
 
# Make a list of 3 dictionaries
Dict= [
    {
        "name": "Ahmed",
        "number": "0505050505"
    },
    {
        "name": "Hamed",
        "number": "0505123123"
    },
    {
        "name": "Nasser",
        "number": "0505051231"
    }
]
print("List of dictionary:", Dict)


Dict.append({"name": "Khaled", "number": "0560560560"})
print("Adding:", Dict)


del Dict[0]["name"]
print("Deleting", Dict)


Dict[-1]["number"] = "0505112233"
print("Update:", Dict)

if "name" in Dict[0]:
    print("There is a name in the firts dictionary")
else:
    print("There is no name in the firts dictionary")


## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.
