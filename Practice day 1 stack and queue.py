# Practice Day-1#

#Stack uses first in last out methodology#
from inspect import stack
import queue


stack=[]
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')

print("initial stack")
print(stack)

print('\n Elements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


#queue uses first in first out methodology#

queue=[]
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
print('initial queue')
print(queue)
print('\n Elements dequeued from queue')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))