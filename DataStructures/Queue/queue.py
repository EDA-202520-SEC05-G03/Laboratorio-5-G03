import queue

def enqueue(my_queue, element=None):
    if element is not None:
        queue.enqueue(my_queue, element)
    return my_queue    

def dequeue(my_queue):
    return queue.dequeue(my_queue)

def peek(my_queue):
    return queue.peek(my_queue)

def is_empty(my_queue):
    return queue.is_empty(my_queue)

def size(my_queue):
    return queue.size(my_queue)

def new_queue():
    return queue.new_queue()
