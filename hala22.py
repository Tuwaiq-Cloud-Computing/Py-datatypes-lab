#answer1
list=["hala","sara","abrar"]
list.append("tuta") #add name in the end list
list.remove("abrar") #remove name from list
list.reverse() #reverse list
list.sort() #sort the list
list.insert(0,"anoud") #to add element in first list
print(list.index(list[-1])) #to print index of last element

#answer2
people = ["Ahmed", "Nasser", "Mohammed"]
print(",".join(people))

#answer3
dic = [{"name": "hala","phone_number":"0538909507"},{"name":"sara","phone_number":"0538909508"},{"name":"tuta","phone_number":"0538909503"}]
dic.append({"name":"najlaa","phone_number":"0555533524"})#add name in the end list
del dic [0]["name"] #delete first
dic[-1]["phone_number"]="055555555" #update last number
if "name" in dic[0]:
    print("The first dictionary has a 'name'")
else:
    print("The first dictionary does not have a 'name'")
