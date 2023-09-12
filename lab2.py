# Q1 > 1-7
print("Q1 Answers")

# 1
list = ["Adeem", "Joud", "Ahmed"]
print(list)

# 2
list.append("Ali"); print(list)

# 3
# removes the specified element
list.remove("Joud"); print(list)
# removes the specified index
list.pop(2); print(list)

# 4
list.reverse(); print(list)

# 5
list.sort(); print(list)

# 6
list.insert(0, "Haneen"); print(list)

# 7
print(list[-1])

# Q2 > 1
print("Q2 Answers")

people = ["Ahmed", "Nasser", "Mohammed"]
print(people)

# 1
print(', '.join(people))

# Q3 > 1-5
print("Q3 Answers")

# 1
contInfo = [
    {
        "name": "Adeem Saleh",
        "phone_number": "0561111111"
    },
    {
        "name": "Joud Ali",
        "phone_number": "0532222222"
    },
    {
        "name": "Ahmad Nasser",
        "phone_number": "0533333333"
    }
]

print(contInfo)

# 2
contInfo.append([
    {"name": "Ali Mohammad",
    "phone_number": "0564444444"}
    ])

print(contInfo)

# 3
contInfo[0].pop("name")
print(contInfo)

# 4
# contInfo[-1]["phone_number"] = "0565555555"
# print(contInfo)

# 5
print("name" in contInfo[0])


