def dicstra(n,edges,src,dst):
    f = collections.defaultdict(dict) # エッジ情報
    # エッジの重みが既存のものより小さい時のみ更新
    for u, v , p in edges:
        if u in f.keys() and v in f[u].keys(): 
            if f[u][v]>p:  
                f[u][v]=p  
                f[v][u]=p
        else:
            f[u][v]=p  
            f[v][u]=p
            
    visited = [False]*n #各ノードに訪れたか
    q = [(0, src)] # 現在の重み，現在位置
    
    #　ダイクストラのアルゴリズム
    while q:
        weight, curr = heapq.heappop(q)
        visited[curr] = True
        if curr == dst:
            return weight
        for next in f[curr]:
            if visited[next] == False: 
                heapq.heappush(q, (weight + f[curr][next], next))
    if visited[dst] == False:
        return "INF"
