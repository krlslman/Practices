#DAY 23 - BST Level-Order Traversal

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
        #Write your code here
        """
        aranacak_nodes = []
        degistirilcek_nodes =""
        aranacak_nodes'a root'u ekle
        node = aranacak_nodes.pop(0)
        bu node'un sol cocugu varsa aranacak_nodes'e ekle,
        bu node'un sag cocugu varsa aranacak_nodes'e ekle,
        """
        aranacak_nodes = list()
        edited_toPrint_nodes = ""
        aranacak_nodes.append(root)
        while len(aranacak_nodes) > 0 :
            node = aranacak_nodes.pop(0)
            if node.left:
                aranacak_nodes.append(node.left)
            if node.right:
                aranacak_nodes.append(node.right)
            edited_toPrint_nodes += str(node.data) + " "
        print(edited_toPrint_nodes)
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
