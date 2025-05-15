k = 0
for i in range(1, 10):
    p = 1
    if i < 6: 
        k = k + 1
    else:
        k = k - 1
    for j in range(1, 6):
        if j >= 6 - k:
            print(p, end="  ")
            p = p + 1
        else:
            print(" ", end="  ")        
    print("")