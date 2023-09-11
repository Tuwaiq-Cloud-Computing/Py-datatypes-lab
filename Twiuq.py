my_list = [1, 3, 2]


my_list.append(1) # Output: [1, 3, 2, 1]
  


popp= my_list.pop() # Output: 1
 


my_list.reverse() # Output: [2, 3, 1]
 


my_list.sort() # Output: [1, 2, 3]
 


my_list.insert(0, 0) # Output: [0, 1, 2, 3]

people = ["Ahmed", "Nasser", "Mohammed"]
x = ",".join(people)
print(x)


# Q3 
dic1 = {
    "Name":"Abdullah",
         "Num":"0550346776"}
dic2 = {"Name":"Ab",
         "Num":"05503"},
dic3 = {"Name":"Abd",
        "Num" : "055034677"}
dic4 = {"Name":"Ahmed",
        "Num":"0550346"}
print(dic1)
dic1.pop("Name")

print(dic1)
print(dic3)
dic3.update({"Num":"05421"})
print(dic3)
dic5= {"name":"Qh",
        "Num":"2124"}
if 'name' in dic1:
    print("The first dictionary has a key called 'name'.")
else:
    print("The first dictionary does not have a key called 'name'")


 