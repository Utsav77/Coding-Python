class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c0=c1=c2=0
        for i in range(len(nums)):
            if(nums[i]==0):
                c0+=1
            elif(nums[i]==1):
                c1+=1
            else:
                c2+=1
                
        for i in range(len(nums)):
            if(c0>0):
                nums[i]=0
                c0-=1
            elif(c1>0):
                nums[i]=1
                c1-=1
            else:
                nums[i]=2
                c2-=1