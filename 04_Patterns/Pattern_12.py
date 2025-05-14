for i in range(1, 6):
    k = 1
    for j in range(1, 10):
        if j >= 6 - i and j <= 4 + i and k==1:
            p = 1
            for s in range(1, i + 1):
                print(f"{int(p):2}", end="  ")
                p = p * (i - s) / s
            k = 0
        else:
            print("", end="  ")
    print("")