# Question 1

list = ["Ruba","Ahmed","Nawaf"]

list.append("Naif")
print(list)

list.pop()
print(list)

list.reverse()
print(list)

list.sort()
print(list)

list.insert(0,"Mohammed")
print(list)

print(list.index("Ruba"))


# Question 2
people = ["Ahmed", "Nasser", "Mohammed"]
print(",".join(people))


# Question 3
contacts = [
    {
        "name": "Ahmed Mohammed",
        "phone_number": "0534827733"
    },
    {
        "name": "Fatima Naif",
        "phone_number": "0588772299"
    },
    {
        "name": "Ruba Mohammed",
        "phone_number": "0599993333"
    }
]

contacts.append({ "name": "Mohammed Khaled", "phone_number": "0534827113"})
print(contacts)

contacts[0].pop("name")
print(contacts)

contacts[-1]["phone_number"] = "0566880000"
print(contacts)

print("name" in contacts[0])