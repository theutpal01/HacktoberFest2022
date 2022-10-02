from typing import List


def bfs(node, level, hashmap):
  if not node:
      return hashmap
  if level not in hashmap:
      hashmap[level] = [node.val]
  else:
      hashmap[level].append(node.val)
  self.bfs(node.left, level + 1, hashmap)
  self.bfs(node.right, level + 1, hashmap)
  return hashmap


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
  if not root:
      return []
  return bfs(root, 0, {}).values()

if __name__ == "__main__":
  print(levelOrder([3,9,20,null,null,15,7])
