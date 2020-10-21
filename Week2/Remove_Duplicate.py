class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        stack = []
        uniq = set()
        
        for char in s:
            if char not in uniq:
                while stack and char < stack[-1] and count[stack[-1]] > 0:
                    uniq.remove(stack.pop())
                stack.append(char)
                uniq.add(char)
            count[char] -= 1
        
        return "".join(stack)