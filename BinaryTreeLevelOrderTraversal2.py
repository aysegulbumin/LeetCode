# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        if root.val==None:
            return []
        level = 0
        LevelDict={}
        LevelDict[level]=[root.val]
        def returnchild(NodeList):
            l = []
            for eachNode in NodeList:
                if eachNode.left!=None:
                    l.append(eachNode.left)
                if eachNode.right!=None:
                    l.append(eachNode.right)
            return l
        def BuildDictionary(NodeList,level):
            level = level + 1
            child = returnchild(NodeList)
            if child == []:
                return
            LevelDict[level]=[]
            for each in child:
                LevelDict[level].append(each.val)
            BuildDictionary(child,level)
        
        BuildDictionary([root],level)
        
        returnlist = []
        
        for elem in LevelDict.values():
            returnlist.append(elem)
        return returnlist[::-1]
