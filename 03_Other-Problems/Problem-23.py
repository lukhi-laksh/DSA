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

        # left side merge
        while left <= mid:
            temp[index] = arr[left]
            left += 1
            index += 1

        # right side merge
        while right <= end:
            temp[index] = arr[right]
            right += 1
            index += 1
        
        for i in range(len(temp)):
            arr[start + i] = temp[i]
        
        return arr




