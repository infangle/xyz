class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for p in s:
            if p == '(':
                stack.append(p)
            else:
                top = stack.pop()
                if top == '(':
                    stack.append(1)
                else:
                    val = 0
                    while top != '(':
                        val += top
                        top = stack.pop()
                    
                    stack.append(val*2)

        return sum(stack)