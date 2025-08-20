class solution():
    def ThreeSum(self, num, target):
        ans = set()
        n = len(num)

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                sum = num[i] + num[left] + num[right]
                if sum == target:
                    ans.add((num[i], num[left], num[right]))
                    left += 1
                    right -= 1
                elif sum > target:
                    right -= 1
                else:
                    left += 1
                    
        return [list(t) for t in ans]

sol = solution()
num = [2, 4, 6, 8, 10, 12, 14, 16, 18]
target = 20
print(sol.ThreeSum(num, target))