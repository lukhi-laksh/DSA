for i in range(1, 8):
    p = 7 - i
    for j in range(1, 8):
        if j <= 8 - i:
            print(p, end="  ")
            p = p - 1
        else:
            print(" ", end="  ")        
    print("")
