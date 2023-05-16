# Py-datatypes-lab

## Tasks:
print("-------Question 1-------")
Flist=[5,2,7] #Make a list with 3 elements
print(Flist)
Flist.append(3) #add an element to the end of list
print(Flist)
del Flist[1]#remove an element from the list
print(Flist)
Flist.reverse()#reverse the list
print(Flist)
Flist.sort()#sort the list
print(Flist)
Flist.insert(0,1)#add an element at the start of the list
print(Flist)
print(Flist[-1])#print the index of the last element

print("-------Question 2-------")
people = ["Ahmed", "Nasser", "Mohammed"]
ken=", ".join(people) #print the list in the following format: Ahmed, Nasser, Mohammed
print(ken)

print("-------Question 3-------")
Kdict={"Kindah":"05123","Sara":"05555","Dema":"05666"}#Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
print(Kdict)
Kdict["Leen"]="05777" #now add 1 more dictionary to the list
print(Kdict)
del Kdict["Kindah"] #now delete the name from the first dictionary
print(Kdict)
Kdict.update({"Leen":"05888"})#update the phone number of the last person
print(Kdict)
print("name" in Kdict)#check if a first dictionary has a key called "name"
print("----------------------------------------------------------------------------")
Question 1:
- Make a list with 3 elements
- add an element to the end of list
- remove an element from the list
- reverse the list
- sort the list 
- add an element at the start of the list
- print the index of the last element


Question 2:
Consider the following list: ``` people = ["Ahmed", "Nasser", "Mohammed"] ```
- print the list in the following format: Ahmed, Nasser, Mohammed
- hint: read about join()

Question 3:
- Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
- now add 1 more dictionary to the list 
- now delete the name from the first dictionary
- update the phone number of the last person
- check if a first dictionary has a key called "name" 


## Submission:

- After finishing the task upload your Python script file to the forked repo and then create a pull request.
