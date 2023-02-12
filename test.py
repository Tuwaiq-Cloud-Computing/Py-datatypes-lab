print("hi")

a = ["riyadh","jeddah","makkah"]

a.append("madena")
print(a)

a.remove(a[3])
print(a)

a.reverse()
print(a)

a.sort()
print(a)

a.insert(0,"hail")
print(a)

print(len(a)-1)  


people = ["Ahmed", "Nasser", "Mohammed"]
str = ','.join([str(item) for item in people])
print(str)



mydictionary= [
    {
        'name': 'soso',
        'phone_number': '1122'
    },
    {
        'name': 'momo',
        'phone_number': '1122'
    },
    {
        'name': 'eoeo',
        'phone_number': '123'
    }
]

mydictionary.append({'name': 'salwa', 'phone_number': '00111'})
print(mydictionary)

del mydictionary[0]['name']
print(mydictionary)

mydictionary[-1]['phone_number'] = '00111'
print(mydictionary)

if "name" in mydictionary[0]:
    print("yes")
else:
    print("no")
