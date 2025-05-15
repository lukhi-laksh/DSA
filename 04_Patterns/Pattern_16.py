for i in range(1, 8):
    for j in range(1, 8):
        if i == j or j + i == 8:
            print(" ", end="  ") 
        else:
            print("*", end="  ")     
    print("")
