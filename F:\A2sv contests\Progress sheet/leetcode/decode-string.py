class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                if s[i] == ']':
                    temp = ""
                    while stack and stack[-1] != '[':
                        temp = stack.pop() + temp
                    stack.pop()
                    d = ''
                    while stack and stack[-1].isdigit():
                        d = stack.pop() + d
                    k = int(d) * temp
                    stack.append(k)

        return ''.join(stack)

            
            
                    

