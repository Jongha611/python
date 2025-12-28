# Frequent error from novice
import math
import numpy as np

# not good
number = [34 ,25, 56, 76, 31, 26]
minimum = math.inf

for n in number:
    if n < minimum:
        minimum = n
print(minimum)

# better solution
minimum = min(number)
maximum = max(number)


# not good
total = 0
num_list = [1, 2, 3, 4, 5]

for i in num_list:
    total += i
avg = total / len(num_list)
print(avg)

# better solution
import numpy as np
avg2 = np.mean(num_list)
print(avg2)


# not good
list1 = [4, 2, 3, 6, 5]
list2 = [5, 2, 7, 4, 1]

a = list1.sort()
b = sorted(list2)

print(a)
print(b)
print(list1)