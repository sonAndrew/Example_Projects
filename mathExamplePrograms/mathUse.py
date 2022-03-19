import math
from functools import reduce

print(list(map(math.sqrt, [9, 25, 36])))

print(list(filter(lambda x: x > 50, [34, 65, 10, 100])))

print(reduce(max, [34, 21, 99, 67, 10]))