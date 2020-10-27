"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root==None:
            return []
        
        returnlist=[]
        returnlist.append(root.val)
        for each in root.children:
            returnlist=returnlist+self.preorder(each)
        return returnlist
