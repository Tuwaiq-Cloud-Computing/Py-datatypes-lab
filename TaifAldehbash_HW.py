########################
#Question 1
#1.1
listQ1= [1,2,3]
#1.2
listQ1.append(5)
#1.3
listQ1.remove(2)
#1.4
listQ1.reverse()
#1.5
listQ1.sort()
#1.6
listQ1.insert(0,0)
#1.7
print((len(listQ1)-1))

########################
#Question 2
people = ["Ahmed", "Nasser", "Mohammed"]
#2.1
x= ", ".join(people)
print(x)

########################
#Question 3
#3.1
listQ3=[{"name":"Nora", "phone_number":"0538188965"}, {"name":"Sara", "phone_number":"0538100965"}, {"name":"Mara", "phone_number":"0530088965"}]
#3.2
listQ3.append({"name": "Seba", "phone_number": "0539761783"})
#3.3
listQ3[0].pop("name")
#3.4
listQ3[-1].update({"phone_number":"0535551763"})
#3.5
print("name" in listQ3[0])