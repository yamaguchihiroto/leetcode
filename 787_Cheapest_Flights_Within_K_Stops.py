class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        f = collections.defaultdict(dict)
        for n, m , p in flights:
            f[n][m]=p  
        q = [(0, src, K+1)]
        while q:
            price, curr, step = heapq.heappop(q)
            if curr == dst:
                return(price)
            if step > 0:
                for next in f[curr]:
                    heapq.heappush(q, (price + f[curr][next], next, step-1))
        return -1
