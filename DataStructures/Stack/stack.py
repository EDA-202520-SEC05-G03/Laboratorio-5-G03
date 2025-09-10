import stack

def new_stack():
    stack = stack.new_stack()
    return stack
def push(element=None):
    stack = stack.push(stack, element)
    return stack
def pop(my_stack):
    elemento = stack.pop(my_stack)
    return elemento
def is_empty(my_stack):
    return stack.is_empty(my_stack)

def top(my_stack):
    elemento = stack.top(my_stack)
    return elemento

def size(my_stack):
    return stack.size(my_stack)