# Python built-in data types

# List: [], mutables
# Dictionary: {}, mutables
# set: {}, immutables
# tuple: (), immutables

# List
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
my_list[1] = 0
print(my_list)

# Dictionary
# As of Python3.7, it is ordered
my_dictionary = {
    "country": "south korea",
    "city": "seoul"
}
print(my_dictionary)
my_dictionary['country'] = "USA"
print(my_dictionary)

# Set
# it is unchangeable, but can add or remove
# cannot subscript: subscript란 인덱스를 가지고 element 하는 것, 즉 요소를 건드리기 위한 접근까진 안된다.
# unique: 같은 요소가 중복으로 들어가지 않는다. {1, 1, 2, 3}x
my_set1 = set((1, 2, 3))
# print(my_set1[1]) # subscript 에러남
print(my_set1)
my_set1.add(1)
print(my_set1)

l = [1, 2, 3, 4, 1, 2, 3, 4]
print(list(set(l)))
my_set2 = {1, 2, 3}
print(my_set2)
my_set2.add(4)
print(my_set2)
my_set2.remove(4)
print(my_set2)


# Tuples
# Once it is created, you cannot change
# it is immutable
# Creation is faster than list
my_tuples = (1, 2, 3)
print(my_tuples[1])