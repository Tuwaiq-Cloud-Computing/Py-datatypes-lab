

print("Answer1:")
drinks = ["Coffee","Tea","Juice"]
drinks.append('Water')
drinks.remove('Tea')
drinks.reverse()
drinks.sort()
drinks.insert(0, 'Crack')
print (len(drinks)  - 1)
print(drinks)

print("Answer2:")
people = ["Ahmed", "Nasser", "Mohammed"]
print(", ".join(people))

print("Answer3:")
Emploies = [{'Name': 'Ali', 'Position': 'Sales'},
  {'Name': 'Mona', 'Position': 'Analyst'}, 
  {'Name': 'Omar', 'Position':'Sales'}]
  
  
NewEmployee = {'Name': 'Hana', 'Position': 'Engineer'}
Emploies.append(NewEmployee)
print(Emploies)
print("                                                     ")
Emploies[0].pop('Name')
print(Emploies)
print("                                                     ")
Emploies[3].update({'Position':'CEO'})
print(Emploies)
print("                                                     ")
Key='Name'
if Key in Emploies[0]:
  print(" Yes, the first dictionary has a key called 'Name'")
else:
  print(" No, first dictionary don't has a key called 'name'")











# num = [1,20]
# def printNum(num):
#     evenlist = []
#     oddlist = []
#    for i in num
#       if (i % 2 == 0):
#          evenlist.append(i)
#       else
#          oddlist.append(i)
# print("EvenList:", evenlist)
# print("OddList: ", oddlist)

 
#     print(num)
    
#     print_num(0, 20)

# for num in range(0, 20):
#    print(num)








