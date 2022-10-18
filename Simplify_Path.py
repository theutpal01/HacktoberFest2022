class Solution(object):
    def simplifyPath(self, path):
        parts = path.split("/")
        stack = []
        for p in parts:
            if p in ['', '.']:
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)
