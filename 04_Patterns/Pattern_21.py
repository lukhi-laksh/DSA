for i in range(1, 5):
    p = 65
    for j in range(1, 8):
        if j >= 5 - i and j <= 3 + i: 
            print(chr(p), end="  ")
            if j < 4:
                p = p + 1
            else:
                p = p - 1
        else:
            print(" ", end="  ")
    print("")