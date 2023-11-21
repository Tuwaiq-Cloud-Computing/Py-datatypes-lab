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
- ---------------------------------------------------------------------
  my_list=[1,2,3]
print (my_list)
my_list.append(4)
print (my_list)
my_list.remove(4)
print (my_list)
my_list.reverse()
print (my_list)
my_list.sort()
print (my_list)
my_list.insert(0,0)
print (my_list)
last_element_index=len(my_list) - 1
print (f"index of the last element ({my_list[last_element_index]}):{last_element_index}")
-------------------------------------------------------------------------------------------
output:
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3]
[3, 2, 1]
[1, 2, 3]
[0, 1, 2, 3]
index of the last element (3):3
___________________________________________________________________________________________________________________________________________________


Question 2:
Consider the following list: ``` people = ["Ahmed", "Nasser", "Mohammed"] ```
- print the list in the following format: Ahmed, Nasser, Mohammed
- hint: read about join()
- -------------------------------------------------------------------------------------
people = ["Ahmed", "Nasser", "Mohammed"]
print(people)
formatted_string=" ,".join(people)
print(formatted_string)
-------------------------------------------------
output:
['Ahmed', 'Nasser', 'Mohammed']
Ahmed ,Nasser ,Mohammed
PS C:\Users\rana_> 
____________________________________________________________________________________________________________________________________________________


Question 3:
- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
- now add 1 more dictionary to the list 
- now delete the name from the first dictionary
- update the phone number of the last person
- check if a first dictionary has a key called "name"
- ------------------------------------------------------------------------
list=[{"name":"rana","phone_number":"12345"},
      {"name":"lolo","phone_number":"34567"},
      {"name":"soso","phone_number":"78966"}]
print (list)
list.append({"name":"roro","phone_number":"23456"})
print(list)
del list[0]["name"]
print(list)
list[-1]["phone_number"]="11111"
print(list)
has_name_key="name"in list[0]
print ("dose the  first dictionary has a key called name ", has_name_key )

-------------------------------------------------------------------------
output:
[{'name': 'rana', 'phone_number': '12345'}, {'name': 'lolo', 'phone_number': '34567'}, {'name': 'soso', 'phone_number': '78966'}]
[{'name': 'rana', 'phone_number': '12345'}, {'name': 'lolo', 'phone_number': '34567'}, {'name': 'soso', 'phone_number': '78966'}, {'name': 'roro', 'phone_number': '23456'}]
[{'phone_number': '12345'}, {'name': 'lolo', 'phone_number': '34567'}, {'name': 'soso', 'phone_number': '78966'}, {'name': 'roro', 'phone_number': '23456'}]
[{'phone_number': '12345'}, {'name': 'lolo', 'phone_number': '34567'}, {'name': 'soso', 'phone_number': '78966'}, {'name': 'roro', 'phone_number': '11111'}]
dose the  first dictionary has a key called name  False


## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.
