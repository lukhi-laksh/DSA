k = 1
for i in range(1, 6):
    for j in range(1, 6):
        if (k % 2 != 0):
            print("* ", end="  ")
        else:
            print("  ", end="  ")
        k = k + 1
    print("")