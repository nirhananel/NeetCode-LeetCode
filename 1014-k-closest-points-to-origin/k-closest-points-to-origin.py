class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq
        from math import sqrt

        distList = []
        for point in points:
            x , y= point

            distance = sqrt(x**2 + y**2)
            heapq.heappush(distList, (distance,point))
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(distList)[1])
        return res
                   