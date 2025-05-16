k = 65
for i in range(1, 6):
    p = k 
    for j in range(1, 6):
        if j >= 6-i: 
            print(chr(p), end="  ")
            p = p - 1
        else:
            print(" ", end="  ")
    print("")
    k += i + 1