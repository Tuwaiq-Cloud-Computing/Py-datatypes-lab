#Question 1:

cities = ["Paris" , "Seoul", "London"] #Make a list with 3 elements

cities.append("Dubai") #add an element to the end of list
cities.remove("Seoul") #remove an element from the list
cities.reverse() #reverse the list
cities.sort() #sort the list
cities.insert(1, "Riyadh") #add an element at the start of the list

print(cities[-1]) #print the index of the last element

#Question 2: 

people = ["Ahmed", "Nasser", "Mohammed"]
peopleString = ','.join(people) #print the list in the following format: Ahmed, Nasser, Mohammed
print(peopleString) #print the list in the following format: Ahmed, Nasser, Mohammed

#Question 3:
info = [{"Name": "Jack", "Phone Num": 590083256}, {"Name": "Bob", "Phone Num": 590067285}, {"Name": "Jake", "Phone Num": 590056855}] #Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
info.append({"Name": "Katilyn", "Phone Num": 596537285}) #now add 1 more dictionary to the list
del info[0]["Name"] #now delete the name from the first dictionary
info[-1]["Phone Num"] = 555555555 #update the phone number of the last person
#check if a first dictionary has a key called "name"
if "Name" in info[0]:
    print("The first dictionary has a key called 'Name'")
else:
    print("The first dictionary does not have a key called 'Name'")