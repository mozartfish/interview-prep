# Stack
# append 
stack = []
stack.append(1)
stack.append(2)

# pop
stack = [1, 2]
# 2
top_element = stack.pop() 

# top 
stack = [1, 2]
# 2
top_element = stack[-1] 

# len 
stack = [1, 2]
while len(stack) > 0:
    print(stack.pop())

# Queue
from collections import deque
queue = deque()
# enqueue
# [1]
queue.append(1) 
# [1, 2]
queue.append(2) 
# dequeue
# pass a list to initialize the queue
queue = deque([1, 2]) 
# [2]
queue.popleft() 
# []
queue.popleft(2) 

# [0][-1]
queue = deque([1, 2, 3, 4])
# 1
leftmost_element = queue[0]
# 4
rightmost_element = queue[-1] 

# len
queue = deque([1, 2])
while len(queue) > 0:
    print(queue.popleft())

