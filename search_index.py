class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(target<=nums[0]):
            return 0
        elif(target>nums[len(nums)-1]):
            return len(nums)
        elif(target==nums[len(nums)-1]):
            return len(nums)-1
        else:
            l=1
            h=len(nums)-1
            while(1):
                m=(l+h)//2
                if(nums[m]==target):
                    return m
                elif(nums[m]>target):
                    if(nums[m-1]<target):
                        return m
                    else:
                        h=m-1
                else:
                    if(nums[m+1]>target):
                        return m+1
                    else:
                        l=m+1