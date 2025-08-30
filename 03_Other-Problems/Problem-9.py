# Custom Stack Functions
stack = []
stackmin = []

# python append() custom function
def pushing(num):
    if len(stack) == 0:
        stack.append(num)
        stackmin.append(num)
    else:
        stack.append(num)
        stackmin.append(min(num, stackmin[-1]))

# python pop function
def poping():
    if len(stack) == 0:
        return -1
    element = stack.pop()
    stackmin.pop
    return element

def getMin():
    if len(stackmin) == 0:
        return -1
    else:
        return stackmin[-1]
    
pushing(5)
print(stack)
print(stackmin)
getMin()
print(stack)
print(stackmin)
pushing(3)
print(stack)
print(stackmin)
getMin()
print(stack)
print(stackmin)
pushing(1)
print(stack)
print(stackmin)
getMin()
print(stack)
print(stackmin)
poping()
print(stack)
print(stackmin)
getMin()
print(stack)
print(stackmin)

