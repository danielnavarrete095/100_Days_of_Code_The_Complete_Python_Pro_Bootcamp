from collections import deque

my_queue = deque()
my_stack = deque()

for i in range (10):
    my_stack.append(i)
    my_queue.append(i)

    # print(f"Stack[0] = {my_stack[0]}")
    # print(f"Queue[0] = {my_queue[0]}")
    # print(f"Stack[-1] = {my_stack[-1]}")
    # print(f"Queue[-1] = {my_queue[-1]}")

for i in range (10):
    my_stack.pop()
    my_queue.popleft()

    # print(f"Stack[0] = {my_stack[0]}")
    # print(f"Queue[0] = {my_queue[0]}")
    # print(f"Stack[-1] = {my_stack[-1]}")
    # print(f"Queue[-1] = {my_queue[-1]}")
