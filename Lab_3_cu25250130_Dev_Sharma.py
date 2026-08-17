# Stack using Linked List

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)
x = stack.pop()
print("Popped:", x)

print("Stack after pop:", stack)

# Queue using Linked List

queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)
x = queue.pop(0)
print("Dequeued:", x)

print("Queue after dequeue:", queue)