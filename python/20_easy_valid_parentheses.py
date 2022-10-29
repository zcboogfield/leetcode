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
    '''
    This is a functional solution that does not manipulate the original input.
    '''
    #Runtime: 54 ms, faster than 61.29% of Python3 online submissions for Valid Parentheses.
    #Memory Usage: 13.8 MB, less than 72.10% of Python3 online submissions for Valid Parentheses.
    def isValid(self, s: str) -> bool:
        openParens = []
        for char in s:
            if char is '{' or char is '[' or char is '(':
                openParens.append(char)
            else: 
                if not openParens or char is not self.pairs[openParens.pop()]:
                    return False
        return not openParens

    def isValidMutation(self, s: str) -> bool:
        return;


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
