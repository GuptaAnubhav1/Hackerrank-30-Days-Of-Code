import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        q= []
        t= root
        while t is not None:
            print(t.data, end= " ")
            if t.left is not None:
                q.append(t.left)
            if t.right is not None:
                q.append(t.right)
            if len(q)!=0:
                t= q.pop(0)
            else:
                break;

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
