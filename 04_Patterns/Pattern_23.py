for i in range(1, 7):
    p = 1
    for j in range(1, 7):
        if j <= i:
            print(p, end="  ")
            p = 1 - p
        else:
            print(" ", end="  ")
    print("")