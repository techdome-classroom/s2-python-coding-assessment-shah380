class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s) - 1):
            if roman_mapping[s[i]] < roman_mapping[s[i + 1]]:
                result -= roman_mapping[s[i]]
            else:
                result += roman_mapping[s[i]]
        if s:  # Check if the string is not empty
            result += roman_mapping[s[-1]]
        return result



