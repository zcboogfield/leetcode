import re
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(re.split('\s+',s.strip())))



run = Solution()

print(run.reverseWords("the sky is blue"))
print(run.reverseWords("  hello world  "))
print(run.reverseWords("a good   example"))
print(run.reverseWords("Alice does not even like bob"))
print(run.reverseWords("  Bob    Loves  Alice   "))



