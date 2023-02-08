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
mylist=["F" , "B" , "C"]
mylist.append("D")
mylist.remove("C")
mylist.sort()
mylist.reverse()
mylist.insert(0 , "U")
#print(mylist)
#print(len(mylist)-1)

Question 2:
Consider the following list: ``` people = ["Ahmed", "Nasser", "Mohammed"] ```
- print the list in the following format: Ahmed, Nasser, Mohammed
- hint: read about join()
list2=["Ahmed", "Nasser", "Mohammed"]
#print(''.join(list2))
Question 3:
- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
- now add 1 more dictionary to the list 
- now delete the name from the first dictionary
- update the phone number of the last person
- check if a first dictionary has a key called "name" 
ParentDict=[ 
     {
    "name" : "Nora",
    "Number" : 5631
  },
  {
    "name" : "Ameera",
    "Number" : 2322
  },
  {
    "name" : "Sara",
    "Number" : 8890
  } ];

print(ParentDict)

ParentDict.append({ 
    "name" : "afrah",
    "Number" : 2007})

print(ParentDict);

ParentDict[0].pop("name");
print(ParentDict)

ParentDict[3].update( { "Number" : 2009 });
print(ParentDict);

if ParentDict[0].keys == "name":
    print("Correct");

else:
    print("Not Correct");

## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.

