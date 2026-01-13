# How memory is managed in Python?

# answer===>   Python manages memory automatically primarily through a private heap space, using reference counting 
# and a generational garbage collector to reclaim unused memory.

a = []
b = []
a.append(b)
b.append(a)
