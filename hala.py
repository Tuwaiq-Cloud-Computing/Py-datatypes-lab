#answer1
list=["hala","sara","abrar"]
print(list)
list.append("tuta")
print(list)
list.remove("abrar")
print(list)
list.reverse()
print(list)
list.sort()
print(list)
list.insert(0,"anoud")
print(list)
print(list.index(list[-1]))

#answer2
people = ["Ahmed", "Nasser", "Mohammed"]
print(",".join(people))

#answer3
dic = [{"name": "hala","phone_number":"0538909507"},{"name":"sara","phone_number":"0538909508"},{"name":"tuta","phone_number":"0538909503"}]
print(dic)
dic.append({"name":"najlaa","phone_number":"0555533524"})
print(dic)
del dic [0]["name"]
print(dic)
dic[-1]["phone_number"]="055555555"
print(dic)
if "name" in dic[0]:
    print("The first dictionary has a 'name' key")
else:
    print("The first dictionary does not have a 'name' key")
