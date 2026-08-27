"""
Lexicographically Smallest Permutation Greater Than Target

"""
class Solution:
    def lexGreaterPermutation(self, s, target):
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        k = 0
        while k < n:
            x = ord(target[k]) - ord('a')

            if cnt[x] == 0:
                break

            cnt[x] -= 1
            k += 1

        if k == n:
            for i in range(n - 1, -1, -1):
                x = ord(target[i]) - ord('a')

                cnt[x] += 1

                for c in range(x + 1, 26):
                    if cnt[c] > 0:
                        ans = target[:i] + chr(c + ord('a'))
                        cnt[c] -= 1

                        for j in range(26):
                            ans += chr(j + ord('a')) * cnt[j]

                        return ans

            return ""

        x = ord(target[k]) - ord('a')

        for c in range(x + 1, 26):
            if cnt[c] > 0:
                ans = target[:k] + chr(c + ord('a'))
                cnt[c] -= 1

                for j in range(26):
                    ans += chr(j + ord('a')) * cnt[j]

                return ans

        for i in range(k - 1, -1, -1):
            x = ord(target[i]) - ord('a')

            cnt[x] += 1

            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    ans = target[:i] + chr(c + ord('a'))
                    cnt[c] -= 1

                    for j in range(26):
                        ans += chr(j + ord('a')) * cnt[j]

                    return ans

        return ""

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""