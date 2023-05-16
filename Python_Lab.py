#Q1
list = [1, 2, 3]

list.append(4)
#print(list)

list.pop(2)
#print(list)

list.reverse()
#print(list)

list.sort()
#print(list)

list.insert(0, 0)
#print(list)

index = list.index(2)
print(index)

#Q2
people = ["Ahmed", "Nasser", "Mohammed"]

var = ","

print(var.join(people))

#Q3
Dic =[
   {"name": "Batool","phone_number": "0539339953",}
   ,{"name": "Samirah","phone_number": "0571234566",}
   ,{"name": "Bayader","phone_number": "0592200599",}
   ]
#print(Dic)

Dic.append({"name": "Fahad","phone_number": "0570007032",})
#print(Dic)

Dic[0].pop('name')
#print(Dic)

Dic[-1]['phone_number']='00000000000'
#print(Dic)

Dic[0]
if 'name' in Dic[0]:
    print('true')
else:
    print('Not found')
