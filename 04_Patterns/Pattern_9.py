for i in range(1, 5):
    ch = 65
    for j in range(1, 8):
        if j <= 5 - i or j >= 3 + i: 
            print(chr(ch), end="  ")
            if(j < 4):
                ch += 1
            else:
                ch -= 1
        else:
            print(" ", end="  ")
            if j < 4:
                ch += 1
            else:
                ch -= 1
    print("")
