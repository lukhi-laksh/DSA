"""
Smallest Divisable Digit Product II

"""
class Solution:
    def smallestNumber(self, num, t):

        temp = t

        for i in range(2, 10):
            while temp % i == 0:
                temp //= i

        if temp > 1:
            return "-1"

        n = len(num)

        rem = [0] * (n + 1)
        rem[0] = t

        pos = n - 1

        numChars = list(num)

        for i in range(n):
            if numChars[i] == '0':
                pos = i
                break

            rem[i + 1] = rem[i] // self.gcd(rem[i], int(numChars[i]))

        if rem[n] == 1:
            return num

        for i in range(pos, -1, -1):

            while True:

                if ord(numChars[i]) >= ord('9'):
                    break

                numChars[i] = chr(ord(numChars[i]) + 1)

                tNow = rem[i] // self.gcd(rem[i], int(numChars[i]))

                k = 9

                ok = True

                for j in range(n - 1, i, -1):

                    while k > 1 and tNow % k != 0:
                        k -= 1

                    if k == 1 and tNow != 1:
                        ok = False
                        break

                    if tNow % k == 0:
                        tNow //= k

                    numChars[j] = str(k)

                if ok and tNow == 1:
                    return "".join(numChars)

        ans = []

        originalT = t

        for i in range(9, 1, -1):
            while originalT % i == 0:
                ans.append(str(i))
                originalT //= i

        padding = max(n + 1 - len(ans), 0)

        ans.extend(['1'] * padding)

        ans.reverse()

        return "".join(ans)

    def gcd(self, a, b):

        while b != 0:
            a, b = b, a % b

        return a

"""

Time Complexity:  O(n² + m)
Space Complexity: O(n + m)

"""