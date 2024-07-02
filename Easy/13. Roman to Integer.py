class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        value = roman[s[-1]]

        for i in range(len(s)-2, -1, -1):
            if roman[s[i]] >= roman[s[i+1]]:
                value += roman[s[i]]
            else:
                value -= roman[s[i]]
        return value
