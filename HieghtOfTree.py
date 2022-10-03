import sys
sys.setrecursionlimit(int(1e6))
class node:
    def __init__(self, data):
        self.data = data
        self.children = []

def takeinput(lst):
    import queue
    q = queue.Queue()
    ind = 0
    rootval = lst[ind]
    ind  += 1
    if rootval == -1:
        return None
    root = node(rootval)
    q.put(root)
    while not q.empty():
        curr = q.get()
        n = lst[ind]
        ind += 1
        for i in range(n):
            child = lst[ind]
            nn = node(child)
            curr.children.append(nn)
            q.put(nn)
            ind += 1
    return root


def findheight(root):
    if root == None:
        return 0
    mx=0
    for i in root.children:
        small_height = findheight(i)
        mx=max(mx,small_height)
    return 1 + mx

lst = list(map(int, input().split()))
root = takeinput(lst)
print(findheight(root))  
