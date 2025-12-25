# Assignment Operator
# Assignment with an = on lists does not make a copy. 
# Instead, assignment makes the two variables point to the one list in memory.

# colors는 리스트 객체를 포인트 했음. b = colors 라는 별개의 카피 객체를 가지고 있는 것이 아니다.
# b와 colors 라는 변수 둘 다 원본 list object의 address를 포인팅 하고 있다.
colors = ["red", "blue", "yellow"]
b = colors

b.append("white")
print(b, colors)

a = [[1, 2], [2, 4]]
b = a[:] # shallow copy

b.append([3, 6])

print(a) # 영향 없음
print(b) # 영향 있음

c = a[:]

c[0].append(7)

print(a) # 영향 있음 (???)
print(c) # 영향 있음
