class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def find_next(s):
            
            result = ""
            count = 0
            current = s[0]
            prev = s[0]
            if len(s)==1:
                return "11"
            for i in range(0,len(s)):
                current=s[i]
                if (current==prev):
                    count +=1
                else:
                    result=result+str(count)+prev
                    count=1
                prev = current
            if(count>0):
                result=result+str(count)+prev
            return result
                
        res = "1"
        for j in range(n-1):
            new=find_next(res)
            res= new
        return res  
                    
