jobs = ["Accounting" , "HR", "Develpers"]

jobs.append("IT")
print(jobs)
jobs.remove("HR")
jobs.reverse()
jobs.sort()
jobs.insert(0,"marketing")
print(jobs)
print(jobs[-1])

people = ["Ahmed", "Nasser", "Mohammed"]
peoplelist = ','.join(people)
print(peoplelist)

data = [{"name": "malek", "phone_num":557744364}, {"name": "khalid", "phone_num": 567743210}, {"name": "ibrahim", "phone_num": 5388769980}]
data.append({"name": "ali", "phone_num": 558863444})
print(data)

del data[0]["name"]
print(data)

data[-1]["phone_num"] = 544377654
print(data)

if "name" in data[0]:
    print("The dictionary has a key name")
else:
    print("The dictionary does n't have a key name")

