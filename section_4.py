# Assignment Operator
# Assignment with an = on lists does not make a copy. 
# Instead, assignment makes the two variables point to the one list in memory.

# colors는 리스트 객체를 포인트 했음. b = colors 라는 별개의 카피 객체를 가지고 있는 것이 아니다.
# b와 colors 라는 변수 둘 다 원본 list object의 address를 포인팅 하고 있다.
colors = ["red", "blue", "yellow"]
b = colors

b.append("white")
print(b, colors)


# Shallow Copy
# A Shallow copy constructs a new compound object and then (to the extent possible) inserts references...
# ...into it to the object found in the original.
a = [[1, 2], [2, 4]]
b = a[:] # shallow copy

b[0].append([3, 6])

print(a)
print(b)

b[0].append(7)

print(a)
print(b)


# Deep Copy
# A deep copy construts a new compound object and then, recursively, inserts copy...
# ...into it of the object found in the original.
import copy

a = [[1, 2], [2, 4]]
b = copy.deepcopy(a) # deep copy

b[0].append(3)

print(a)
print(b)