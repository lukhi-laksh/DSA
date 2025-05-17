for i in range(1, 6):
    k = 69
    for j in range(1, 6):
        if j <= i:
            print(chr(k), end="  ")
            k = k - 1
        else:
            print(" ", end="  ")
    print("")                   