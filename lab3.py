#Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
MyList = [
    {"Name": "Amal", "Phone_number": "055638291"},
    {"Name": "Noura", "Phone_number": "054745211"},
    {"Name": "Ali", "Phone_number": "055578921"}
]
print(MyList)

#now add 1 more dictionary to the list 
MyList.append({"Name": "Khalid", "Phone_number": "055555768"})
print(MyList)

# now delete the name from the first dictionary
del MyList[0]["Name"]
print(MyList)

#update the phone number of the last person
MyList[-1]["Phone_number"] = "055564322"
print(MyList)

# Check if the first dictionary has a key called "name"
if "name" in MyList[0]:
    print("The first dictionary has a key called 'Name'")
else:
    print("The first dictionary does not have a key called 'Name'")
    