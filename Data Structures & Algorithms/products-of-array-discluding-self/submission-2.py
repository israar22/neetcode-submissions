class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            a=1
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    a=a*nums[j]
            res.append(a)
        return res
                

        