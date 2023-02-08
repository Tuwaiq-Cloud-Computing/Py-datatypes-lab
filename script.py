#Question1
list1 = ["A","B","C"]
list1.append("D")   #add in the end
list1.remove("A")   #remove from list
list1.reverse()     #reverse
list1.sort()        #sort
list1.insert(0,"E") #add to the start
print(len(list1)-1) #index of the last element


#Question2
people = ["Ahmed", "Nasser", "Mohammed"]
print(", ".join(people))


#Question3
list2 =[
    {
        "name":"Ali",
        "phone_number":'0511111111'
    },
    {
        "name":"Saad",
        "phone_number":'0522222222'
    },
    {
        "name":"Fahad",
        "phone_number":'0533333333'
    }
]

list2.append({
        "name":"Sarah",
        "phone_number":'0544444444'
})  #add dictionary to the list

list2[0].pop("name")    #delete name from the first dictionary
list2[len(list2)-1].update({"phone_number":'0555555555'})   #update the phone number of the last person

if list2[0].keys == "name": #check if a first dictionary has a key called "name"
    print("name found")
else:
    print("not found")

