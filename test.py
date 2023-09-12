#Q1
alpha = ['a','b','c']
alpha.append('d')
print(alpha)
alpha.pop(0)
print(alpha)
alpha.reverse()
print(alpha)
alpha.sort()
print(alpha)
alpha.insert(0, 'a')
print(alpha)
print(alpha.index('d'))

#Q2

people = ["Ahmed", "Nasser", "Mohammed"]
formatted_list = ", ".join(people)
print(formatted_list)

#Q3 

dic=[{"name":"basmah" ,"phone_number":"0535215993" },
     {"name":"sara", "phone_number": "0535215995" },
     { "name":"maha","phone_number":"0535215996"}  ]


dic.append({"name": "amal", "phone_number": "0535215997"})

# Delete the name key from the first dictionary
del dic[0]["name"]

# Update the phone number of the last person
dic[-1]["phone_number"] = "0535215998"

# Check if the first dictionary has a key called "name"
if "name" in dic[0]:
    print("The first dictionary has the key 'name'.")
else:
    print("The first dictionary does not have the key 'name'.")
                                                  