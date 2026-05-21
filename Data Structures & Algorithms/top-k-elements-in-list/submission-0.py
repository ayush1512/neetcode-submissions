class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        count = sorted(count.items(),key=lambda item:item[1],reverse=True)
        # print(count)
        res = []
        for i in range(0,k):
            res.append(count[i][0])
        return res

