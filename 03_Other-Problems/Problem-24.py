stack = []

# Custome Append
def pushing(num):
    if len(stack) == 0:
        stack.append((num * 100) + num)

    else:
        stack.append(num * 100 + min(stack[-1] % 100, num))

# Custom pop last index
def poping():
    if len(stack) == 0:
        return -1
    return stack.pop()

# return fast index 
def getMin():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1] % 100

pushing(5)
print(getMin())   # 5
