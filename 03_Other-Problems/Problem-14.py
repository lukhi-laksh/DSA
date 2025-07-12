# Declare String
s = "ababc"
# Create empty list
count = list()

# Outer loop
for i in range(len(s)):
    arr = list()
    # Inner loop
    for j in range(i, len(s)):
        if j in arr:
            break
        arr.append(j)
        count.append(len(arr))
print(max(count))

    
