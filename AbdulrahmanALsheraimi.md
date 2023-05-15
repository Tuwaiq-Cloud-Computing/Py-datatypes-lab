#Question 1

list = [2, 0, 1]

list.append(1)

list.pop(1)

list.reverse()

list.sort()

list.insert(0, 0)

index = list.index(2)

print(index)


#Question 2

people = ["Ahmed", "Nasser", "Mohammed"]

A = " "

print(A.join(people))



#Question 3


A = {"name": "Abdulrahman", "phone_number": "786587656875"}

LastPerson = {'phone_number': '000000000'}

A.update(LastPerson)

A["age"] = "23"
A.pop("name")


print(A)

x = 'name' in A
print(x)


