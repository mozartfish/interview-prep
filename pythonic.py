point1 = [0, 0]
point2 = [2, 4]

# unpacking
x1, y1 = point1 # x1 = 0, y1 = 0
x2, y2 = point2 # x2 = 2, y2 = 4
slope = (y2 - y1) / (x2 - x1)
print(slope)

# regular 
x1, y1 = point1[0], point1[1]
x2, y2 = point2[0], point2[1]

# value error thrown when there are not enough variables on the left side for unpacking
# x, y = [0, 0, 0]

# loop unpacking 
points = [[0, 0], [2, 4], [3, 6], [5, 10]]
for x, y in points:
    print(f"x: {x}, y: {y}")

# regular loop unpacking 
for point in points:
    x, y = point[0], point[1]
    print(f"x: {x}, y: {y}")

# enumerate - index, value 
nums = [2, 7, 9, 2]
for i, n in enumerate(nums):
    print(i, n)

# zip 
names = ['Alice', 'Bob', 'Charlie', 'David']
scores = [90, 85, 88, 92]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# inequality
 # shorthand multiple comparisons 
x = 5
if 0 < x and x < 10:
    print('x is between 0 and 10')

 # regular multiple comparisons 
x = 5
if 0 < x and x < 10:
    print('x is between 0 and 10')

# min-max 
# builtin min-max 
transactions = -2
transactions = max(0, transactions)

# regular min-max
transactions = -2
if transactions < 0:
    transactions = 0



