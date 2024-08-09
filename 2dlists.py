# example 
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 2d list of integers 
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# [1, 2, 3]
print(nested_list[0])  
# [4, 5, 6]
print(nested_list[1]) 
# [7, 8, 9] 
print(nested_list[2])  

# access elements in the lists 
# 1
print(nested_list[0][0])  
# 9
print(nested_list[2][2])  
# 6
print(nested_list[1][2])  

# lists of different length 
nested_list = [[1], [2, 3], [4, 5, 6]]
for sublist in nested_list:
    for element in sublist:
        print(element)

# grid 
grid = [
    [0, 0, 0],
    [0, 0, 0]
]

# 2 
rows = len(grid) 
# 3
cols = len(grid[0]) 

# initializing grids 
# list comprehension 
# columns -> 3, rows -> 2
grid = [[0 for i in range(3)] for j in range(2)]
grid[0][0] = 1
# [[1, 0, 0], [0, 0, 0]]
print(grid) 

# concise list comprehension 
# columns -> 3, rows -> 2
grid = [[0] * 3 for _ in range(2)]
