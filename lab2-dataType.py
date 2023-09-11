# Question 1

list = ["Shada","Abduallah","Sultan"]

list.append("Ahmed")
print(list)

# ["Shada","Abduallah","Sultan","Ahmed"]

list.pop(0)
print(list)

# ["Abduallah","Sultan","Ahmed"]

list.reverse()
print(list)

# ['Ahmed', 'Sultan', 'Abduallah']

list.sort()
print(list)

# ['Abduallah', 'Ahmed', 'Sultan']

list.insert(0,"Nada")
print(list)

# ['Nada', 'Abduallah', 'Ahmed', 'Sultan']

print(list.index("Sultan"))

# 3

# Question 2
people = ["Ahmed", "Nasser", "Mohammed"]
print(",".join(people))
 
# Ahmed,Nasser,Mohammed

# Question 3
contacts = [
    {
        "name": "Shada Alwethairi",
        "phone_number": "0512345678"
    },
    {
        "name": "Abduallah Alwethairi",
        "phone_number": "0587654321"
    },
    {
        "name": "Sultan Alwethairi",
        "phone_number": "0512121234"
    }
]

contacts.append({ "name": "Nada Mohammed", "phone_number": "0523232324"})
print(contacts)

# [{'name': 'Shada Alwethairi', 'phone_number': '0512345678'}, {'name': 'Abduallah Alwethairi', 'phone_number': '0587654321'}, {'name': 'Sultan Alwethairi', 'phone_number': '0512121234'}, {'name': 'Nada Mohammed', 'phone_number': '0523232324'}]

contacts[0].pop("name")
print(contacts)

# [{'phone_number': '0512345678'}, {'name': 'Abduallah Alwethairi', 'phone_number': '0587654321'}, {'name': 'Sultan Alwethairi', 'phone_number': '0512121234'}, {'name': 'Nada Mohammed', 'phone_number': '0523232324'}]

contacts[-1]["phone_number"] = "0599999899"
print(contacts)

# [{'phone_number': '0512345678'}, {'name': 'Abduallah Alwethairi', 'phone_number': '0587654321'}, {'name': 'Sultan Alwethairi', 'phone_number': '0512121234'}, {'name': 'Nada Mohammed', 'phone_number': '0599999899'}]

print("name" in contacts[0])