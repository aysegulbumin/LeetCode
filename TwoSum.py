class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        IndexDict={}
        for i in range(len(nums)):
            if target-nums[i] not in IndexDict:
                #add the num[i] into IndexDict
                IndexDict[nums[i]]=i
            else:
                index= IndexDict[target-nums[i]]
                return [index,i]
        return []
