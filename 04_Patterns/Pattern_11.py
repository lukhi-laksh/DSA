k = 0
for i in range(1, 8):
    if (i <= 4):
        k = k + 1
    else:
        k = k - 1
    for j in range(1, 5):
        if j <= k: 
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print("")
