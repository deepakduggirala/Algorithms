import heapq
def djikstra(S):
    Visited = [False for i in range(N+1)]
    Distance = [float('inf') for i in range(N+1)]
    Distance[S] = 0
    heap = []
    heapq.heappush(heap,(0,S))
    for i in xrange(1,N+1):
        if heap:
            while(True):
                _,u = heapq.heappop(heap)
                if not Visited[u]:
                    break
            Visited[u] = True
            for v,weight_uv in a[u]:
                if not Visited[v]:
                    if Distance[v] > Distance[u] + weight_uv:
                        Distance[v] = Distance[u] + weight_uv
                        heapq.heappush(heap, (Distance[v],v))
    print Distance
    return Distance
