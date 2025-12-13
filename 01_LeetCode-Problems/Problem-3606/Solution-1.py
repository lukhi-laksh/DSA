"""
Coupon Code Validator

"""

class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):

        def is_valid_name(s):
            if s == "":
                return False

            letters = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM"
            numbers = "1234567890"
            symbols = "_"
            for c in s:
                if c not in letters and c not in numbers and c not in symbols:
                    return False
            return True

        def is_valid_business_line(s):
            return s in ["electronics", "grocery", "pharmacy", "restaurant"]

        valid = []
        for i in range(len(code)):
            if is_valid_business_line(businessLine[i]) and \
                is_valid_name(code[i]) and \
                isActive[i]:
                valid.append((code[i], businessLine[i]),)

        el = []
        gr = []
        ph = []
        rest = []

        for valid_code, valid_bl in valid:
            if valid_bl == "electronics":
                el.append(valid_code)

            if valid_bl == "grocery":
                gr.append(valid_code)

            if valid_bl == "pharmacy":
                ph.append(valid_code)

            if valid_bl == "restaurant":
                rest.append(valid_code)

        return sorted(el) + sorted(gr) + sorted(ph) + sorted(rest)

"""
Time Complexity: O(n · L + n log n)
Space Complexity: O(n)

"""