# Py-datatypes-lab

## Tasks:

Question 1:
- Make a list with 3 elements
list=['Hajar',4,5.6]
print(list)

- add an element to the end of list
list=['Hajar',4,5.6]
list.append('sara')
print(list)

- remove an element from the list
list=['Hajar',4,5.6]
list.remove(4)
print(list)

- reverse the list
list=['Hajar',4,5.6]
list.reverse()
print(list)

- sort the list 
list=['Hajar','fatimah','Amirah']
list.sort()
print(list)

- add an element at the start of the list
list=['Hajar',4,5.6]
list.insert(0,'fatimah')
print(list)

- print the index of the last element
list=['Hajar',4,5.6]
print(list[2])

Question 2:
Consider the following list: ``` people = ["Ahmed", "Nasser", "Mohammed"] ```
- print the list in the following format: Ahmed, Nasser, Mohammed
- hint: read about join()
people=['Ahmed','Nasser','Mohammed']
x="#".join(people)
print(x)

Question 3:
- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
employee1 =('Hajar','0558953018','data analysis')
employee1={'name':'Hajar', 'phone_number':'0558953018', 'job':'data analysis'}
print(employee1.values())

employee2 =('Amirah','05589648710','DBA')
employee2={'name':'Amirah', 'phone_number':'05589648710', 'job':'DBA'}
print(employee2.values())

employee3 =('Sara','05589648710','system analysis')
employee3={'name':'sara', 'phone_number':'0508745356', 'job':'system analysis'}
print(employee3.values())

- now add 1 more dictionary to the list 
employee4 =('Reem','0505674321','Software Engineer')
employee4={'name':'Reem', 'phone_number':'0505674321', 'job':'Software Engineer'}
print(employee4.values())

- now delete the name from the first dictionary
employee1 =('Hajar','0558953018','data analysis')
employee1={'name':'Hajar', 'phone_number':'0558953018', 'job':'data analysis'}
del employee1['name']
print(employee1.values())

- update the phone number of the last person
employee3 =('Sara','05589648710','system analysis')
employee3={'name':'sara', 'phone_number':'0508745356', 'job':'system analysis'}
employee3.update({'phone_number':'0567854312'})
print(employee3.values())

- check if a first dictionary has a key called "name" 
employees1 =('Hajar','0558953018','data analysis')
employee1={'name':'Hajar', 'phone_number':'0558953018', 'job':'data analysis'}
print(employee1['name'])


## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.
