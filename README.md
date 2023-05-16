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
 listT = [1, 2, 3]
listT.append("star")
listT.remove(2)
listT.reverse()
listT.sort()
listT.insert(0,"H1")
print (listT[3])



Question 2:
Consider the following list: ``` people = ["Ahmed", "Nasser", "Mohammed"] ```
- print the list in the following format: Ahmed, Nasser, Mohammed
- hint: read about join()
people1 = ["Ahmed", "Nasser", "Mohammed"]
people3 = people1 + listT
print(people3)


Question 3:
- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
- now add 1 more dictionary to the list 
- now delete the name from the first dictionary
- update the phone number of the last person
- check if a first dictionary has a key called "name" 
dict =  {
  "name": "shames",
  "age": "five",
  "phone_number" : "11221997"
}
dict["color"] = "gold"
dict.pop("name")
dict.update({"phone_number": 19972211})
if "name" in dict.keys():
  print ("Y")
else:
  print ("N")
print(dict)



## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.
