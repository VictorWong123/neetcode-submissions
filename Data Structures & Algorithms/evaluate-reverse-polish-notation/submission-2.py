class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators= "+/-*"
        for token in tokens: 
            if token in operators:
                if token == "+":                
                    x, y = stack.pop(), stack.pop()
                    z = x+y
                elif token=="-":
                    x, y = stack.pop(), stack.pop()
                    z = y-x

                elif token=="/":
                    x, y = stack.pop(), stack.pop()
                    z = int(float(y)/x)

                elif token=="*":
                    x, y = stack.pop(), stack.pop()
                    z = x*y

                stack.append(z)
            else: 
                stack.append(int(token))
            print(stack)
        return stack[0]





        