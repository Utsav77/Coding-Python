class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l=0
        n=len(citations)
        h=n-1
        if(n==0):
            return 0

        while(l<=h):
            m=(l+h)//2
            if(citations[m]>=n-m):
                h=m-1
            else:
                l=m+1
        return n-l