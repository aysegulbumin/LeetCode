class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        temp = [[]]
        
        for each in nums:
            for o in output:
                 temp.append(o + [each])
            output=[]
            for l in temp:
                output.append(l)
        return output
