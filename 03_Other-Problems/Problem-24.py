stack = []

def pushing(num):
    if len(stack) == 0:
        stack.append((num * 100) + num)

    else:
        stack.append(num * 100 + min(stack[-1] % 100, num))
        
def poping():
    if len(stack) == 0:
        return -1
    return stack.pop()

def getMin():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1] % 100

pushing(5)
print(getMin())   # 5
