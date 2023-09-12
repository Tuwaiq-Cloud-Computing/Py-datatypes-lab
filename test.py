#Q1:
list = [2 , 3 , 5]

list.append(7)
print(list)

list.pop(2)
print(list)

list.reverse()
print( list)

list.sort()
print( list)

list.insert(0,9)
print(list)

print(len(list) - 1)

#Q2:
people = ["Ahmed", "Nasser", "Mohammed"]
print( ', '.join(people))

#Q3:
contacts = [
    {
        'name': 'Atheer',
        'phone_number': '1234567890'
    },
    {
        'name': 'Hoor',
        'phone_number': '9876543210'
    },
    {
        'name': 'Alaia',
        'phone_number': '5555555555'
    }
]

contacts.append({'name': 'Sara', 'phone_number': '999888777'})

del contacts[0]['name']

contacts[-1]['phone_number'] = '111222333'

has_name_key = 'name' in contacts[0]

for contact in contacts:
    print(f"Name: {contact.get('name', 'N/A')}")
    print(f"Phone Number: {contact['phone_number']}")
    print()

print("First dictionary has 'name' key:", has_name_key)
