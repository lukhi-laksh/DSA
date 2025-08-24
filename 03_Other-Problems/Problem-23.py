def laksh(arr, start, end):
    def Merge(arr, start, mid, end):
        temp = [0] * (end - start + 1)
        left = start
        right = mid + 1
        index = 0

        # saperate array
        while left <= mid and right <= end:
            if arr[left] <= arr[right]:
                temp[index] = arr[left]
                left += 1
            else:
                temp[index] = arr[right]
                right += 1
            index += 1






