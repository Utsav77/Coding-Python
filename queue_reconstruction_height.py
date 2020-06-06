class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        a=[]
        people.sort(key = lambda a: (-a[0], a[1]))
        for i in people:
            a.insert(i[1],i)
        return a