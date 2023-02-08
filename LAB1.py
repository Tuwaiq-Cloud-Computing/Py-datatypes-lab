#Q1
MyList1 = [1,2,3]
MyList1.append(4)
MyList1.remove(2)
MyList1.reverse()
MyList1.sort()
MyList1.insert(0,1)
print(MyList1)
print(len(MyList1)-1)

#Q2
people = ["Ahmed", "Nasser", "Mohammed"]
x = ","
z = x.join(people)
print(z)

#Q3
MyList2 = [{"name": "Rand",
"phone_number": "0500000000"},

 {"name": "Sara",
  "phone_number": "0511111111"},
  
  {"name": "Arwa",
  "phone_number": "0522222222"}]

Dic3 = {"name": "Ali",
         "phone_number": "0533333333"}
MyList2.append(Dic3)

MyList2[0].pop("name")
print(MyList2)

MyList2[3].update({"phone_number": "0544444444"})
print(MyList2)

if "name" in MyList2:
    print("Exists")
else:
    print("Dose not exist")    

