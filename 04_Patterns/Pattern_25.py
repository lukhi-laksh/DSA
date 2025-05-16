m = 0

for i in range(1, 22):  # i from 1 to 21
    if i <= 11:
        m += 1
    else:
        m -= 1

    k = m - 1

    for j in range(1, 22):
        if j >= 12 - m and j <= 10 + m:
            if j < 11:
                print(f" {k % 10}", end="")
                k += 1
            else:
                print(f" {k % 10}", end="")
                k -= 1
        else:
            print("  ", end="")  
    print()
