print("Question 1")

mylist=[2,3,4]
mylist.append(5)
mylist.remove(3)
mylist.reverse()
mylist.sort()
mylist.insert(0,1)
print(len(mylist)-1)

print("Question 2")
people = ["Ahmed", "Nasser", "Mohammed"]

print(' ,'.join(people))

print("Question 3")

lsDict = [{'name': 'Ashwaq', 'phoneNumber': '05555555'},
          {'name': 'Abdullah', 'phoneNumber': '05555555'},
          {'name': 'Norah', 'phoneNumber': '05555555'}]
more={'name':'Khaled','phoneNumber': '05555555'}
lsDict.append(more)
print(lsDict)

lsDict[0].pop('name')
print(lsDict)

lsDict[3].update({'phoneNumber':'0566666'})
print(lsDict)

key='name'
if key in lsDict[0]:
    print(" found")
else:
    print("Not found")
