f = collections.defaultdict(dict)
for u, v , p in edges:
    f[u][v]=p  
for dst in range(n):
    visited = [False]*n
    q = [(0, src)]
    while q:
        weight, curr = heapq.heappop(q)
        visited[curr] = True
        if curr == dst:
            print(weight)
            break
        for next in f[curr]:
            if visited[next] == False: 
                heapq.heappush(q, (weight + f[curr][next], next))
    if visited[dst] == False:
        print("INF")
    
