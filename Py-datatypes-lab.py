#Q1
# Create a list with 3 elements
list = [1, 2, 3]
print(list)

# Add an element to the end of the list
list.append(4)
print(list)

# Remove an element from the list
del list[0] 
print(list)


# Reverse the list
list.reverse()
print(list)

# Sort the list
list.sort()
print(list)

#insert an element at the start
list.insert(0,1)
print(list)

# Print the index of the last element
last_element_index = len(list) - 1
print(last_element_index)

#Q2
people = ["Ahmed", "Nasser", "Mohammed"]

format_list = ", ".join(people)

print(format_list)


#Q3
# list of dictionaries
main_list = [
    {"name": "Nawaf", "phone_number": "0560544677"},
    {"name": "Khaled", "phone_number": "0558975521"},
    {"name": "Turki", "phone_number": "0504319993"}
]
print("")
print(main_list)

# Add one dictionary to the list
new_person = {"name": "Abdulaziz", "phone_number": "0598400676"}
main_list.append(new_person)

print("")
print(main_list)

# Delete the "name" from the first dictionary
del main_list[0]["name"]

print("")
print("Deleting the name of the first index " ,main_list)

# Update the phone number of the last person
main_list[-1]["phone_number"] = "0558888888"

print("")
print("Updating phone number", main_list)

#Checking if the first dictionary has a key called "name"
checking = "name" in main_list[0]

# Print the updated list and the result of the check
print("")
print("Updated List:", main_list)
print("Does the first dictionary have a key called 'name'?", checking)

