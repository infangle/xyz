class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        p = path.split('/')
        for i in p:
            if i == '..' and stack:
                stack.pop()
            elif i != '.' and i != '' and i != '..':
                stack.append(i)
    
        if not stack:
            return '/'
        else:
            return '/' + '/'.join(stack)
                    