# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import math
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        if A==None:
            return []
        level = 0
        LevelDict={}
        LevelDict[level]=[A.val]
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
        BuildDictionary([A],level)
        returnlist = []
        for elem in LevelDict.values():
            returnlist.append(elem)
        return returnlist
