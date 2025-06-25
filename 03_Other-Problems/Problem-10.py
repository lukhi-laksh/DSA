stack = []

def pushing(num):
    if len(stack) == 0:
        stack.append(num)
        stackmin.append(num)
    else:
        stack.append(num)
        stackmin.append(min(num, stackmin[-1]))

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
