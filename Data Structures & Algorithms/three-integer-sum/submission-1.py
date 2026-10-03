class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and nums[0]+nums[1]+nums[2] == 0:
            return [nums]
        else:
            res = []
            nums.sort()
            for i in range(len(nums)-2):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                j, k = i+1, len(nums)-1
                while j<k:
                    sum = nums[i]+nums[j]+nums[k]
                    if sum == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        while j<k and nums[j]==nums[j+1]:
                            j=j+1
                        while j<k and nums[k]==nums[k-1]:
                            k=k-1
                        j+=1
                        k-=1
                    elif sum > 0:
                        k=k-1
                    else:
                        j=j+1
            return res