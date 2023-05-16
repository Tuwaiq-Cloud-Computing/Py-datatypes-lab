# Py-datatypes-lab

## Tasks:

Question 1:
- Make a list with 3 elements
 list = [1, 2 , 3]
 print(list)
- add an element to the end of list
 list.append(4) 
 print(list)
- remove an element from the list
 list.remove(1) 
 print(list)
- reverse the list
 list.reverse()
 print(list)
- sort the list 
 list.sort()
 print(list)
- add an element at the start of the list
  list.insert(0,1)
  print(list)
- print the index of the last element
 last_elem = list[-1]
 print(last_elem) 


Question 2:
Consider the following list: ``` people = ["Ahmed", "Nasser", "Mohammed"] ```
- print the list in the following format: Ahmed, Nasser, Mohammed
- hint: read about join()

people = ["Ahmed", "Nasser", "Mohammed"]
names = ", ".join(people)
print(names) 

Question 3:

- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
 ls_dict = [{'name' : "amal", 'phone_num' : "0544657907"} , 
           {'name' : "sara", 'phone_num' : "0556789909"} , 
           {'name' : "nora", 'phone_num' : "0123456785"}]
           
- now add 1 more dictionary to the list
 ls_dict = {'name' : "nouf"}
 
- now delete the name from the first dictionary
 del ls_dict["name"]
print(ls_dict)
- update the phone number of the last person
 ls_dict.update()
- check if a first dictionary has a key called "name" 
 if 'name' in ls_dict.keys():
  print "true"
else:
  print "false"


## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.
