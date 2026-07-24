class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        product=[]
        

        for i in range(n):
            res=1
            for j in range(n):
                if i==j:
                    continue
                else:
                    res=res*nums[j]
            product.append(res)
        return product
        


        