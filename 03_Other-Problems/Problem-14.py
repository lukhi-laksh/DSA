# Declare String
s = "ababc"
count = list()
for i in range(len(s)):
    arr = list()
    for j in range(i, len(s)):
        if j in arr:
            break
        arr.append(j)
        count.append(len(arr))
print(max(count))

    
