num = 1
for i in range(1, 6):
    flag = 1
    temp = []
    for j in range(1, 2 * i):
        if flag == 1:
            temp.append(num)
            num += 1
            flag = 0
        else:
            temp.append("*")
            flag = 1

    if i % 2 == 0:
        temp = temp[::-1]

    for j in range(1, 10):
        if j <= 2 * i - 1:
            print(temp[j - 1], end="  ")
        else:
            print(" ", end="  ")
    print("")
