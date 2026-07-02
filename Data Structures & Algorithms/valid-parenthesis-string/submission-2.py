class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        stack = []


        for j in range(len(s)):
            i = s[j]
            if i=="(":
                stack.append(j)
            elif stack and i ==")":
                stack.pop()
            elif star and i==")":
                star.pop()
            elif i=="*":
                star.append(j)
            else:
                return False
        
        if len(stack)> len(star):
            return False

        while stack:
            x = stack.pop()
            y = star.pop()
            if x>y:
                return False
                
        return True

            
                
       
