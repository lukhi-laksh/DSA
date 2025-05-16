for i in range(1, 6):
    k = i
    for j in range(1, 6):
        if j <= i:
            print(k, end="  ")
            k = k - 1
        else:
            print(" ", end="  ")
    print("")                   