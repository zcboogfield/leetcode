'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
'''
class Solution:
    pairs = { 
             '{':'}',
             '[':']',
             '(':')' 
    }
    openers = pairs.keys()

    #Runtime: 73 ms, faster than 9.26% of Python3 online submissions for Valid Parentheses.
    #Memory Usage: 13.8 MB, less than 72.10% of Python3 online submissions for Valid Parentheses.
    def isValid(self, s: str) -> bool:
        openParens = []
        for char in s:
            if char in self.openers:
                openParens.append(char)
            else: 
                if not openParens or char is not self.pairs[openParens[-1]]:
                    return False
                else:
                    openParens.pop(-1)
        return not openParens

run = Solution()

print(run.isValid("()"))
# Output: Frue
print(run.isValid("()[]{}"))
# Output: Frue
print(run.isValid("(]"))
# Output: False
print(run.isValid("([{}])"))
# Output: True
print(run.isValid("]"))
# Output: False


