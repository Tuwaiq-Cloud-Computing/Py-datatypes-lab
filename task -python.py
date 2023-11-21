# Question 1
list=[20 , 30 , 40 ]
print("basic list = " , list)
list.append(50)
print("List after add = ", list)
list.remove(20)
print("List after remove = ", list)
list.reverse()
print("List Reversed = ", list)
list.sort()
print("List Sort = ", list)
list.insert(0,"100")
print("List after insert = " , list)
print("List after the index of the last element =  ", list[-1])
# Question 2
people = ["Ahmed", "Nasser", "Mohammed"]
A_list = ",".join(people)
print(A_list)
# Question 3
people = [
    {"name": "Aziz", "phone_number": "1234567890"},
    {"name": "Fares", "phone_number": "9876543210"},
    {"name": "Mohannd", "phone_number": "5555555555"}
]
print("Basic List = ")
print(people)
people.append( {"name": "Ziad", "phone_number": "0123344558"})
print("List after add = ", people)
del people[0]
print("List after Delete = ", people)
people[-1]["phone_number"] = "1111122222"
print("List after updating  = ")
print(people)
people = "name" in people[0]
print("List after check has 'name'?")
print(people)


