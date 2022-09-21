# Conisder the following list: list = [2, 0, 1, 0] According to the question, write down the code or the output

# Notes: These are not sequential, the code is only affecting the original list. Answers should only be 1 line long

# Output: 4
from traceback import print_tb


list = [2, 0, 1, 0]
#code:print(len(list))

# Output: 2
# Code: print(list[0])

# Output: 2
#code:print(list.count(0))

# Output: index out of range nore the list index
# Code: print(list[4])

# Output: True
# Code: 2 in list

# Output: [2, 0, 1, 0, 'A']
# Code: list.append("A")
#print(list)

# Output: [0, 0, 1, 2]
# Code: ?
# print(list)
# list[0]=0
# list[-1]=2
# print(list)

# Output: [2, 0, 1]
# Code: ?
# print(list)
# list.pop(-1)
# print(list)
# Output: [0, 1]
# Code: ?
# list.pop(0)
# list.pop(-1)
# print(list)

# Output: [0, 1, 0, 2]
# Code: ?
list.reverse()
print(list)


