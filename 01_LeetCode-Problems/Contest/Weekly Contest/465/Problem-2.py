class Solution(object):
    def splitNumber(n, k):

        factor_list = []
        current = n
        divisor = 2

        while divisor * divisor <= current:
            while current % divisor == 0:
                factor_list.append(divisor)
                current //= divisor
            divisor += 1
        if current > 1:
            factor_list.append(current)

        split_parts = [1] * k

        for factor in factor_list:
            min_index = 0
            for i in range(k):
                if split_parts[i] < split_parts[min_index]:
                    min_index = i
            split_parts[min_index] *= factor

        return split_parts