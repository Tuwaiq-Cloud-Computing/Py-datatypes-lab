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

ver = ","
print(ver.join(people1))


Question 3:
- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
- now add 1 more dictionary to the list 
- now delete the name from the first dictionary
- update the phone number of the last person
- check if a first dictionary has a key called "name" 
dict1 =	{
  "name": "shames",
  "age": "5",
  "phone_number" : "11221997"}
dict1["color"] = "gold"
dict1.pop("name")
dict1.update({"phone_number": 19972211})
if "name" in dict1.keys():
  print ("Y")
else:
  print ("N")
print(dict1)
dict2 =	{
  "name": "nem",
  "age": "7",
  "phone_number" : "228759"}
dict2["color"] = "white"
dict2.pop("name")
dict2.update({"phone_number": 5578391})
if "name" in dict2.keys():
  print ("Y")
else:
  print ("N")
print(dict)
dict3 =	{
  "name": "jed",
  "age": "20",
  "phone_number" : "5342935"}
dict3["color"] = "red"
dict3.pop("name")
dict3.update({"phone_number": 5492349})
if "name" in dict3.keys():
  print ("Y")
else:
  print ("N")
print(dict3)



## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.
