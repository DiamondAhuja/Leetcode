class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paran = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []
        if len(s) % 2 != 0:
            return False

        for bracket in s:
            if bracket in paran:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                comparison = paran[stack.pop()]
                if bracket == comparison:
                    continue
                return False

        return len(stack) == 0
