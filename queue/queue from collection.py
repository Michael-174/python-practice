from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
print("initial queue is", q)
print(q.popleft())
print(q.popleft())
print(q)


