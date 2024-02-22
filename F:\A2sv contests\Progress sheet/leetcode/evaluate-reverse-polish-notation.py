class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t != '+' and t != '-' and t != '*' and t != '/':
                stack.append(int(t))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(b - a)
                elif t == '*':
                    stack.append(a*b)
                elif t == '/':
                    if a * b > 0:
                        stack.append(math.floor(b / a))
                    else:
                        stack.append(math.ceil(b / a))

        return int(stack.pop())