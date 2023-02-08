 
#Qustion1   
people = [1, 2 ,3]

people.append(4)
print(people)

people.remove(2)
print(people)

people.reverse()
print(people)

people.sort()
print(people)

people.insert(0, 10)
print(people)

print(len(people)-1)

#Qustion2
people2 = ["Ahmed", "Nasser", "Mohammed"]
print(' , '.join(people2))

#Qustion3
dictionary = [{"name": "Rawan", "Phone_number": "050631455"} , 
              {"name": "Remaz", "Phone_number": "050639455" },
              {"name": "lolo", "Phone_number":  "050831455"}]


##Add
dic4 = {
    "name": "Ruba",
   "phone_number": "0506314355",
}

dictionary.append(dic4)
print(dictionary)

##delet
del dictionary[0]["name"]
print(dictionary)

##update
dictionary[0]["phone_number"] = "000000000"

##check
if "name" in dictionary[0]:
    print("done")
else :
    print("not found")
    
   