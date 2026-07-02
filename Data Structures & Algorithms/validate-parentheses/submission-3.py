class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'{':"}",
                    "[":"]",
                    "(":")"
        }
        for i in s:
            print(stack)
            if i in hashmap.keys():
                stack.append(i)
            else: 
                if not stack:
                    return False
                if i == hashmap[stack[-1]]:
                    stack.pop()
                else:
                    return False


        if not stack:
            return True
        else:
            return False
            