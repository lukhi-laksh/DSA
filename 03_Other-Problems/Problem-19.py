arr = [2, 7, 11, 15, 27]
target = 22

ans = []
start = 0
end = len(arr) - 1

while start < end:
    curr_sum = arr[start] + arr[end]
    if curr_sum == target:
        ans.append([arr[start], arr[end]])
        break
    elif curr_sum < target:
        start += 1
    else:
        end -= 1

print(ans)
