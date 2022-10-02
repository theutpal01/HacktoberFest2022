from typing import List


class TreeNode:


    def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
        

    def insertIntoBST(self, root, val):
      if not root:
        return TreeNode(val)
      if val < root.val:
        root.left = self.insertIntoBST(root.left, val)
      else:
        root.right = self.insertIntoBST(root.right, val)
      return root


    def bfs(self, node, level, hashmap):
      if not node:
        return hashmap
      if level not in hashmap:
        hashmap[level] = [node.val]
      else:
        hashmap[level].append(node.val)
      self.bfs(node.left, level + 1, hashmap)
      self.bfs(node.right, level + 1, hashmap)
      return hashmap


    def levelOrder(self, root) -> List[List[int]]:
      if not root:
        return []
      return list(self.bfs(root, 0, {}).values())


if __name__ == "__main__":

  tree = TreeNode(10)
  nums = [5, 11, 12, 34, 3, 1]
  
  for num in nums:
    tree.insertIntoBST(tree, num)

  print(tree.levelOrder(tree))
