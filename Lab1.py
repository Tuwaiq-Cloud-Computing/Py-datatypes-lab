#Question 1
product = ["Phone" , "Laptop" , "Ipad"]
print(product)

product.append("Headphones")
print(product)

product.remove("Laptop")
print(product)

product.reverse()
print(product)

product.sort()
print(product)

product.insert(0,"Charger")
print(product)

print(len(product)-1)


#Question 2
people = ["Ahmed", "Nasser", "Mohammed"]
x= ","
print(x.join(people))


#Qestion 3\
All_Dict = [{"name": "Remaz" , "Phone_Number":"0505905054"} ,
{"name": "Fatma" , "Phone_Number":"0555424291"} ,
 {"name": "Abdulkareem" , "Phone_Number":"0500181166"}]

Dict4 = {"name": "Atheer" , "Phone_Number":"0500989466"}
All_Dict.append(Dict4)
print(All_Dict)

del All_Dict[0]["name"]
print(All_Dict)

All_Dict[3]["Phone_Number"]= " 0000000000"
print(All_Dict)

if "name" in All_Dict[0]:
    print("the key aleardy created")
else:
    print("Not found")